import logging
import os
import tempfile
from csv import DictReader
from zipfile import ZipFile

import frontmatter
import requests
from flask.cli import AppGroup
from sqlalchemy import and_, update

from application.extensions import db
from application.models import Specification

logger = logging.getLogger(__name__)
info_handler = logging.StreamHandler()
error_handler = logging.FileHandler("error.log")
info_handler.setLevel(logging.INFO)
error_handler.setLevel(logging.ERROR)

logger.addHandler(info_handler)
logger.addHandler(error_handler)

data_cli = AppGroup("data")

foreign_keys = {
    "attribution",
    "datatype",
    "licence",
    "specification_status",
    "typology",
    "dataset",
    "field",
    "specification",
}


@data_cli.command("load")
def load_data():
    spec_zip_url = (
        "https://github.com/digital-land/specification/archive/refs/heads/main.zip"
    )

    with tempfile.TemporaryDirectory() as tmp_dir:
        logger.info(f"Created temp directory {tmp_dir}")

        resp = requests.get(spec_zip_url)
        zip_file_path = os.path.join(tmp_dir, "main.zip")

        with open(zip_file_path, "wb") as f:
            f.write(resp.content)

        with ZipFile(zip_file_path) as config_zip:
            config_zip.extractall(path=tmp_dir)
            for table in db.metadata.sorted_tables:
                csv_name = f"{table.name.replace('_', '-')}.csv"
                csv_file_path = os.path.join(
                    tmp_dir, f"specification-main/specification/{csv_name}"
                )
                if os.path.exists(csv_file_path):
                    logger.info(f"Loading {csv_file_path}")
                    with open(csv_file_path) as f:
                        for i, row in enumerate(DictReader(f)):
                            insert_row = _get_insert_row(table, row)
                            try:
                                db.session.execute(table.insert(), insert_row)
                                db.session.commit()
                            except Exception as e:
                                logger.error(
                                    f"Error inserting row {i} of {os.path.basename(f.name)} into {table.name}"
                                )
                                logger.error(e)
                                db.session.rollback()

            # load the typology and specification join tables
            _load_typology_field(tmp_dir)
            _load_specification_dataset(tmp_dir)

            # load the specification markdown and diagram
            _load_specification_markdown(tmp_dir)
            _load_specification_diagram(tmp_dir)


def _load_typology_field(tmp_dir):
    fields_csv = os.path.join(tmp_dir, "specification-main/specification/field.csv")
    typology_field = db.metadata.tables["typology_field"]
    with open(fields_csv) as f:
        for i, row in enumerate(DictReader(f)):
            r = {"field": row["field"], "typology": row["typology"]}
            try:
                db.session.execute(typology_field.insert(), r)
                db.session.commit()
            except Exception as e:
                logger.error(
                    f"Error inserting row {i} of field.csv into typology_field"
                )
                logger.error(e)
                db.session.rollback()


def _load_specification_dataset(tmp_dir):
    specification_csv = os.path.join(
        tmp_dir, "specification-main/specification/specification.csv"
    )
    specification_dataset = db.metadata.tables["specification_dataset"]
    with open(specification_csv) as f:
        for i, row in enumerate(DictReader(f)):
            datasets = row["datasets"].split(";")
            for d in datasets:
                r = {"specification_id": row["specification"], "dataset_id": d}
                try:
                    db.session.execute(specification_dataset.insert(), r)
                    db.session.commit()
                except Exception as e:
                    logger.error(
                        f"Error inserting row {i} of specification.csv into specification_dataset"
                    )
                    logger.error(e)
                    db.session.rollback()

        specification_dataset_field = db.metadata.tables["specification_dataset_field"]
        for specification in Specification.query.all():
            for sd in specification.specification_datasets:
                for f in sd.dataset.dataset_fields:
                    r = {
                        "specification": specification.specification,
                        "dataset": sd.dataset.dataset,
                        "field": f.field.field,
                    }
                    try:
                        db.session.execute(specification_dataset_field.insert(), r)
                        db.session.commit()
                    except Exception as e:
                        logger.error(
                            f"Error inserting row {r} into specification_dataset_field"
                        )
                        logger.error(e)
                        db.session.rollback()


def _load_specification_markdown(tmp_dir):
    markdown_dir = os.path.join(tmp_dir, "specification-main/content/specification")
    for specification in Specification.query.all():
        markdown_path = os.path.join(markdown_dir, f"{specification.specification}.md")
        if os.path.exists(markdown_path):
            print(
                f"fetching infor from markdown {markdown_path} for {specification.specification}"
            )
            front_matter = frontmatter.load(markdown_path)
            if front_matter.get("plural"):
                specification.plural = front_matter.get("plural")
                db.session.add(specification)

            dataset_field = db.metadata.tables["dataset_field"]
            datasets = front_matter.get("datasets")
            for dataset in datasets:
                fields = dataset.get("fields")
                for field in fields:
                    description = field.get("description")
                    if description:
                        stmt = (
                            update(dataset_field)
                            .where(
                                and_(
                                    dataset_field.c.dataset_id == dataset["dataset"],
                                    dataset_field.c.field_id == field["field"],
                                )
                            )
                            .values(description=description)
                        )
                        db.session.execute(stmt)
                        db.session.commit()

    if db.session.dirty:
        db.session.commit()


def _load_specification_diagram(tmp_dir):
    content_dir = os.path.join(tmp_dir, "specification-main/docs/specification")
    for specification in Specification.query.all():
        svg_path = os.path.join(
            content_dir, f"{specification.specification}/diagram.svg"
        )
        if os.path.exists(svg_path):
            print(f"fetching {specification.specification} diagram from {svg_path}")
            with open(svg_path) as f:
                svg_content = f.read()
                specification.diagram = svg_content
                db.session.add(specification)

    if db.session.dirty:
        db.session.commit()


@data_cli.command("drop")
def drop_data():
    for table in reversed(db.metadata.sorted_tables):
        db.session.execute(table.delete())
        db.session.commit()
    print("data dropped")


def _get_insert_row(table, row):
    insert_row = {}
    for key, val in row.items():
        k = key.replace("-", "_")
        if k in foreign_keys and k != table.name:
            k = f"{k}_id"
        if not val:
            v = None
        else:
            v = val
        insert_row[k] = v
    return insert_row
