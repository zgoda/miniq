from peewee import CharField

from .app import db


class User(db.Model):
    name = CharField(max_length=200, unique=True)
