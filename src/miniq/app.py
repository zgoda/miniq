from peewee import SqliteDatabase
from playhouse.flask_utils import FlaskDB

from . import config
from .utils import Application

app = Application(__name__.split('.')[0])
app.config.from_object(config)

db = FlaskDB(
    app,
    SqliteDatabase(
        app.config['DB_NAME'],
        pragmas={
            'journal_mode': 'wal',
            'cache_size': -1 * 64000,
            'foreign_keys': 1,
            'ignore_check_constraints': 0,
        }
    )
)
