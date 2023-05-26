from flask import Blueprint, render_template

from application.models import Dataset, Datatype, Field, Specification, Typology

spec = Blueprint("specification", __name__, url_prefix="/specification")


@spec.route("/")
def specifications():
    working_drafts = Specification.query.filter(
        Specification.specification_status_id == "working-draft"
    ).all()
    page_data = {
        "title": "Specifications",
        "lede": "Technical specifications to help Local Planning Authorities provide consistent planning data.",
        "working_drafts": working_drafts,
        "page_header": True,
    }
    return render_template("specifications.html", **page_data)


@spec.route("/<string:specification>/")
def specification(specification):
    specification = Specification.query.get(specification)
    page_data = {
        "caption": "Specification",
        "title": specification.name,
        "lede": f"A technical specification for {specification.name} planning data",
        "specification": specification,
    }
    return render_template("specification.html", **page_data)


@spec.route("/dataset")
def datasets():
    page_data = {"title": "Datasets", "datasets": Dataset.query.all()}
    return render_template("datasets.html", **page_data)


@spec.route("/dataset/<string:dataset>")
def dataset(dataset):
    ds = Dataset.query.get(dataset)
    page_data = {"title": "Dataset", "dataset": ds}
    return render_template("dataset.html", **page_data)


@spec.route("/field")
def fields():
    fields = Field.query.all()
    page_data = {"title": "Fields", "fields": fields}
    return render_template("fields.html", **page_data)


@spec.route("/field/<string:field>")
def field(field):
    f = Field.query.get(field)
    page_data = {
        "title": "Field",
        "field": f,
    }
    return render_template("field.html", **page_data)


@spec.route("/datatype")
def datatypes():
    datatypes = Datatype.query.all()
    page_data = {"title": "Datatypes", "datatypes": datatypes}
    return render_template("datatypes.html", **page_data)


@spec.route("/datatype/<string:datatype>")
def datatype(datatype):
    d = Datatype.query.get(datatype)
    fields = Field.query.filter(Field.datatype_id == d.datatype).all()
    page_data = {
        "title": "Datatype",
        "subtitle": d.name,
        "datatype": d,
        "fields": fields,
    }
    return render_template("datatype.html", **page_data)


@spec.route("/typology")
def typologies():
    typologies = Typology.query.all()
    page_data = {"title": "Typologies", "typologies": typologies}
    return render_template("typologies.html", **page_data)


@spec.route("/typology/<string:typology>")
def typology(typology):
    t = Typology.query.get(typology)
    datatypes = set([f.datatype for f in t.fields])
    page_data = {
        "title": "Typology",
        "subtitle": t.name,
        "typology": t,
        "datatypes": datatypes,
    }
    return render_template("typology.html", **page_data)
