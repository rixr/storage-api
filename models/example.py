import datetime
import peewee as pe
from models.base import EnvModel
from models.auth import User


class ExampleRecord(EnvModel):
    user = pe.ForeignKeyField(User, backref='username')
    data = pe.CharField()
    created_at = pe.DateTimeField(default=datetime.datetime.now)
