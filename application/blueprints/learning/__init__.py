from flask import Blueprint, render_template, request, url_for, flash
from application.models import *
import random


learning = Blueprint('learning', __name__, template_folder='templates')


@learning.route('/<level>')
def learning_start(level):
    themes = Theme.query.filter(Theme.level_id == level).all()
    return render_template('/learning/learning_level.html', themes=themes)

@learning.route('/<level>/<theme_id>')
def theme(level, theme_id):
    name = Theme.query.filter(Theme.id == theme_id).first().name
    return render_template('/learning/learning_map.html', level=level, theme_id=theme_id, name=name)

@learning.route('/<level>/<theme_id>/quantities')
def quantities(level, theme_id):
    quantities = Quantity.query.filter(Quantity.theme_id == theme_id).all()
    return render_template('/learning/quantities.html', quantities=quantities, level=level, theme_id=theme_id)

@learning.route('/<level>/<theme_id>/symbols_test')
def symbol_test(level, theme_id):
    q = random.choice(Quantity.query.filter(Quantity.theme_id == theme_id).all())
    questions = random.sample(Quantity.query.filter(Quantity.id != q.id).all(), k=3)
    questions.append(q)
    random.shuffle(questions)   
    return render_template('/learning/symbol_test.html', questions=questions, correct=q, level=level, theme_id=theme_id)

@learning.route('/<level>/<theme_id>/units_test')
def unit_test(level, theme_id):
    q = random.choice(Quantity.query.filter(Quantity.theme_id == theme_id).all())
    questions = random.sample(Quantity.query.filter(Quantity.id != q.id).all(), k=3)
    questions.append(q)
    random.shuffle(questions)   
    return render_template('/learning/unit_test.html', questions=questions, correct=q, level=level, theme_id=theme_id)

@learning.route('/<level>/<theme_id>/formulas')
def formulas(level, theme_id):
    formulas = Formula.query.filter(Quantity.theme_id == theme_id).all()
    return render_template('/learning/formulas.html', formulas=formulas, level=level, theme_id=theme_id)

@learning.route('/<level>/<theme_id>/formuls_test')
def formul_test(level, theme_id):
    f = random.choice(Formula.query.filter(Formula.theme_id == theme_id).all())
    formulas = random.sample(Formula.query.filter((Formula.id != f.id) & (Formula.name != f.name)).all(), k = 3)
    formulas.append(f)
    random.shuffle(formulas)
    return render_template('/learning/formula_test.html', formulas=formulas, correct=f, level=level, theme_id=theme_id)
