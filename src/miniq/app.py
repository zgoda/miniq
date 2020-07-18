from pony.flask import Pony
from pony.orm import Database

from . import config
from .utils import Application

app = Application(__name__.split('.')[0])
app.config.from_object(config)

db = Database()
Pony(app)
