from flask import Blueprint, abort, render_template

from application.models import Specification

guide = Blueprint("guidance", __name__, url_prefix="/guidance")


themes = [
    "Guidance for local planning authorities",
    "Data specification guidance",
    "Other guidance",
]


titles = {
    "introduction": "Introduction for local planning authorities",
    "how-to-provide-data": "How to provide data",
}


@guide.route("/")
def guidance():
    page_data = {
        "page_title": "Guidance for local planning authorities",
        "themes": themes,
        "page_name": "home",
    }
    return render_template("guidance/index.html", **page_data)


@guide.route("/<string:page_name>")
def page(page_name):
    page_data = {
        "page_title": titles[page_name],
        "themes": themes,
        "page_name": page_name,
    }
    return render_template(f"guidance/{page_name}.html", **page_data)


@guide.route("/specifications/")
def specifications():
    page_data = {
        "page_title": "Data specifications for local planning authorities",
        "themes": themes,
        "page_name": "specifications",
    }
    return render_template("guidance/specifications/index.html", **page_data)


@guide.route("/specifications/<string:specification_id>")
def specification(specification_id):
    specification = Specification.query.get(specification_id)
    if specification is None:
        return abort(404)
    dataset_count = len(specification.datasets)
    page_data = {
        "page_title": specification.name,
        "themes": themes,
        "dataset_count": dataset_count,
        "specification": specification,
    }
    return render_template("guidance/specifications/specification.html", **page_data)
