from application import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from slugify import Slugify, CYRILLIC

slugify_ru = Slugify(pretranslate=CYRILLIC)



roles_users = db.Table("roles_users",
                       Column("user_id", Integer, ForeignKey('user.id')),
                       Column("role_id", Integer, ForeignKey("role.id"))
                       )


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    active = Column(Boolean)
    roles = db.relationship("Role", secondary=roles_users, backref=db.backref("users", lazy='dynamic'))

    def __init__(self, email, password):
        self.email = email,
        self.password_hash = generate_password_hash(password)
        



class Role(db.Model):
    id = Column(Integer, primary_key=True)
    role = Column(String, unique=True)




    



class Level(db.Model):
    id = Column(Integer, primary_key=True)
    level = Column(String)
    page_title = Column(String)
    slug = Column(String, unique=True)
    themes = db.relationship('Theme', backref='level')

    def __repr__(self) -> str:
        return self.level


class Theme(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    level_id = Column(Integer, ForeignKey('level.id'))
    quantities = db.relationship('Quantity', backref='theme')
    formuls = db.relationship('Formula', backref='theme')
    def __repr__(self) -> str:
        return self.name
    

class Quantity(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    symbol = Column(String)
    unit = Column(String)
    theme_id = Column(Integer, ForeignKey('theme.id'))


class Formula(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    formula = Column(String)
    theme_id = Column(Integer, ForeignKey('theme.id'))


