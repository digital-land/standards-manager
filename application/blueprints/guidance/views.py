from flask import Blueprint, render_template

guide = Blueprint("guidance", __name__, url_prefix="/guidance")


@guide.route("/")
def guidance():
    page_data = {"title": "Guidance for local planning authorities"}
    return render_template("guidance/index.html", page_data=page_data)
