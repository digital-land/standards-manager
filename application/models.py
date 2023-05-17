from sqlalchemy.dialects.postgresql import JSON

from application.extensions import db


class DateModel(db.Model):
    __abstract__ = True

    entry_date = db.Column(db.Date)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)


# For the time being these classes represent other
# registers used by standards data model


class Licence(DateModel):
    licence = db.Column(db.Text, primary_key=True)
    text = db.Column(db.Text)


class Attribution(DateModel):
    attribution = db.Column(db.Text, primary_key=True)
    text = db.Column(db.Text)


class SpecificationStatus(DateModel):
    specification_status = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)


class ProjectStatus(DateModel):
    project_status = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)


class Theme(DateModel):
    theme = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)


class Realm(DateModel):
    name = db.Column(db.Text, primary_key=True)  # ? no key field listed in spec repo
    reference = db.Column(db.Text)
    description = db.Column(db.Text)


class ProvisionReason(DateModel):
    provision_reason = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)


# end stub registers


# TODO - does this need a description field?
dataset_field = db.Table(
    "dataset_field",
    db.Column("dataset", db.Text, db.ForeignKey("dataset.dataset"), primary_key=True),
    db.Column("field", db.Text, db.ForeignKey("field.field"), primary_key=True),
    db.Column("guidance", db.Text),
    db.Column("hint", db.Text),
    db.Column("entry_date", db.Date),
    db.Column("start_date", db.Date),
    db.Column("end_date", db.Date),
)

specification_dataset = db.Table(
    "specification_dataset",
    db.Column("dataset", db.Text, db.ForeignKey("dataset.dataset"), primary_key=True),
    db.Column(
        "specification",
        db.Text,
        db.ForeignKey("specification.specification"),
        primary_key=True,
    ),
    db.Column("entry_date", db.Date),
    db.Column("start_date", db.Date),
    db.Column("end_date", db.Date),
)

specification_dataset_field = db.Table(
    "specification_dataset_field",
    db.Column("dataset", db.Text, db.ForeignKey("dataset.dataset"), primary_key=True),
    db.Column(
        "specification",
        db.Text,
        db.ForeignKey("specification.specification"),
        primary_key=True,
    ),
    db.Column("field", db.Text, db.ForeignKey("field.field"), primary_key=True),
    db.Column("guidance", db.Text),
)

typology_field = db.Table(
    "typology_field",
    db.Column(
        "typology", db.Text, db.ForeignKey("typology.typology"), primary_key=True
    ),
    db.Column("field", db.Text, db.ForeignKey("field.field"), primary_key=True),
    db.Column("entry_date", db.Date),
    db.Column("start_date", db.Date),
    db.Column("end_date", db.Date),
)


class Specification(DateModel):
    specification = db.Column(db.Text, primary_key=True)
    specification_status_id = db.Column(
        db.Text, db.ForeignKey("specification_status.specification_status")
    )
    # whatever else needed here
    datasets = db.relationship(
        "Dataset", secondary=specification_dataset, lazy="subquery"
    )


class Dataset(DateModel):
    dataset = db.Column(db.Text, primary_key=True)
    attribution_id = db.Column(db.Text, db.ForeignKey("attribution.attribution"))
    collection = db.Column(db.Text)
    description = db.Column(db.Text)
    key_field = db.Column(db.Text)
    entity_minimum = db.Column(db.BigInteger)
    entity_maximum = db.Column(db.BigInteger)
    licence_id = db.Column(db.Text, db.ForeignKey("licence.licence"))
    name = db.Column(db.Text)
    paint_options = db.Column(JSON)
    plural = db.Column(db.Text)
    phase = db.Column(db.Text)
    prefix = db.Column(db.Text)
    realm = db.Column(db.Text)
    text = db.Column(db.Text)
    themes = db.Column(db.Text)
    typology_id = db.Column(db.Text, db.ForeignKey("typology.typology"))
    typology = db.relationship("Typology")
    wikidata = db.Column(db.Text)
    wikipedia = db.Column(db.Text)
    fields = db.relationship("Field", secondary=dataset_field, lazy="subquery")


class Typology(DateModel):
    typology = db.Column(db.Text, primary_key=True, nullable=False)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    text = db.Column(db.Text)
    plural = db.Column(db.Text)
    wikidata = db.Column(db.Text)
    wikipedia = db.Column(db.Text)
    fields = db.relationship(
        "Field", secondary=typology_field, lazy="subquery", back_populates="typologies"
    )


class Field(DateModel):
    field = db.Column(db.Text, primary_key=True, nullable=False)
    name = db.Column(db.Text)
    datatype_id = db.Column(db.Text, db.ForeignKey("datatype.datatype"), nullable=True)
    typologies = db.relationship(
        "Typology", secondary=typology_field, lazy="subquery", back_populates="fields"
    )


class Datatype(DateModel):
    datatype = db.Column(db.Text, primary_key=True, nullable=False)
    name = db.Column(db.Text)
    text = db.Column(db.Text)
