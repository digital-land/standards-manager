from flask import Blueprint, render_template

from application.models import Specification

spec = Blueprint("specification", __name__, url_prefix="/specification")


@spec.route("/specification/")
def specifications():
    working_drafts = Specification.query.filter(
        Specification.specification_status_id == "working-draft"
    ).all()
    return render_template("specifications.html", working_drafts=working_drafts)


@spec.route("/specification/<string:specification>/")
def specification(specification):
    specification = Specification.query.get(specification)
    return render_template("specification.html", specification=specification)
