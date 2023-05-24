from flask import Blueprint, render_template

from application.models import Dataset, Specification

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


@spec.route("/dataset/<string:dataset>/")
def dataset(dataset):
    ds = Dataset.query.get(dataset)
    page_data = {"title": "Dataset"}
    return render_template("dataset.html", dataset=ds, page_data=page_data)

