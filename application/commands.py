import logging
import os
import tempfile
from csv import DictReader
from zipfile import ZipFile

import requests
from flask.cli import AppGroup

from application.extensions import db

logger = logging.getLogger(__name__)
info_handler = logging.StreamHandler()
error_handler = logging.FileHandler("error.log")
info_handler.setLevel(logging.INFO)
error_handler.setLevel(logging.ERROR)

logger.addHandler(info_handler)
logger.addHandler(error_handler)

data_cli = AppGroup("data")


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


@data_cli.command("drop")
def drop_data():
    for table in reversed(db.metadata.sorted_tables):
        db.session.execute(table.delete())
        db.session.commit()


def _get_insert_row(table, row):
    insert_row = {}
    for key, val in row.items():
        k = key.replace("-", "_")
        if not val:
            v = None
        else:
            v = val
        insert_row[k] = v
    return insert_row
