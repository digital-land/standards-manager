from flask import Blueprint, render_template

from application.models import Specification

spec = Blueprint("specification", __name__, url_prefix="/specification")


@spec.route("/")
def specifications():
    page_data = {
        "title": "Specifications",
        "lede": "Technical specifications to help Local Planning Authorities provide consistent planning data.",
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
    return render_template("specification.html", specification=specification)
