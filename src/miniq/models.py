import os

from pony.orm import Required

from .app import db


class User(db.Entity):
    name = Required(str, 200)
    password = Required(str)


db.bind(provider='sqlite', filename=os.getenv('DB_FILENAME', ':memory'), create_db=True)
db.generate_mapping(create_tables=True)
