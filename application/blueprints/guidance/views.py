from flask import Blueprint, render_template

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


@guide.route("/specifications/<string:specification_name>")
def specification(specification_name):
    page_title = f"{specification_name.replace('-', ' ').title()} data"
    page_data = {
        "page_title": page_title,
        "themes": themes,
        "page_name": specification_name,
    }
    return render_template(
        f"guidance/specifications/{specification_name}.html", **page_data
    )
