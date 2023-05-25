from flask import Blueprint, render_template

from application.models import Dataset, Datatype, Field, Specification, Typology

spec = Blueprint("specification", __name__, url_prefix="/specification")


@spec.route("/")
def specifications():
    page_data = {
        "title": "Specifications",
        "lede": "Technical specifications to help Local Planning Authorities provide consistent planning data.",
        "config": {"page_header": True},
    }
    working_drafts = Specification.query.filter(
        Specification.specification_status_id == "working-draft"
    ).all()
    return render_template(
        "specifications.html", working_drafts=working_drafts, page_data=page_data
    )


@spec.route("/<string:specification>/")
def specification(specification):
    specification = Specification.query.get(specification)
    page_data = {
        "caption": "Specification",
        "title": specification.name,
        "lede": "A technical specification for "
        + specification.name
        + " planning data",
        "config": {},
    }
    return render_template(
        "specification.html", specification=specification, page_data=page_data
    )


@spec.route("/dataset")
def datasets():
    page_data = {"title": "Datasets"}
    return render_template(
        "datasets.html", datasets=Dataset.query.all(), page_data=page_data
    )


@spec.route("/dataset/<string:dataset>")
def dataset(dataset):
    ds = Dataset.query.get(dataset)
    page_data = {"title": "Dataset"}
    return render_template("dataset.html", dataset=ds, page_data=page_data)


@spec.route("/field")
def fields():
    fields = Field.query.all()
    page_data = {"title": "Fields"}
    return render_template("fields.html", fields=fields, page_data=page_data)


@spec.route("/field/<string:field>")
def field(field):
    f = Field.query.get(field)
    page_data = {
        "title": "Field",
    }
    return render_template("field.html", field=f, page_data=page_data)


@spec.route("/datatype")
def datatypes():
    page_data = {"title": "Datatypes"}
    datatypes = Datatype.query.all()
    return render_template("datatypes.html", page_data=page_data, datatypes=datatypes)


@spec.route("/datatype/<string:datatype>")
def datatype(datatype):
    d = Datatype.query.get(datatype)
    fields = Field.query.filter(Field.datatype_id == d.datatype).all()
    page_data = {"title": "Datatype", "subtitle": d.name}
    return render_template(
        "datatype.html", page_data=page_data, datatype=d, fields=fields
    )


@spec.route("/typology")
def typologies():
    page_data = {"title": "Typologies"}
    typologies = Typology.query.all()
    return render_template(
        "typologies.html", page_data=page_data, typologies=typologies
    )


@spec.route("/typology/<string:typology>")
def typology(typology):
    t = Typology.query.get(typology)
    datatypes = set([f.datatype for f in t.fields])
    page_data = {"title": "Typology", "subtitle": t.name}
    return render_template(
        "typology.html", page_data=page_data, typology=t, datatypes=datatypes
    )
