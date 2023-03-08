from application import app, db
from flask import render_template, request, redirect, url_for
from application.models import *
from flask_login import login_required, login_user
import random
from slugify import Slugify, CYRILLIC

slugify_ru = Slugify(pretranslate=CYRILLIC)


@app.route('/')
def main_page():
    themes = Level.query.all()
    return render_template("main.html", themes=themes)

@app.route('/theory')
def theory():
    return render_template("theory.html")



    




# @app.route("/create_quantity", methods = ["POST", "GET"])
# @login_required
# def new_quantity():
#     if request.method == "POST":
#         name = request.form.get("name")
#         label = request.form.get("label")
#         unit = request.form.get("unit")
#         level = request.form.get("level")
#         db.session.add(Quantity(name, label, unit, level))
#         db.session.commit()
#         return render_template("new_quantity.html")
#     else:
#         return render_template("create_quantity.html")



