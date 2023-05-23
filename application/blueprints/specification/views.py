from flask import Blueprint, render_template

spec = Blueprint("specification", __name__, url_prefix="/specification")


@spec.route("/specification/")
def specifications():
    return render_template("specifications.html")


@spec.route("/specification/<string:specification>/")
def specification():
    return render_template("specification.html")
