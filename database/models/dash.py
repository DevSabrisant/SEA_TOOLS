from peewee import Model, IntegerField, CharField
from database.database import db

class Dash(Model):

    titulo = CharField()
    homepage = IntegerField(default=0)
    homepage2 = IntegerField(default=0)
    homepage3 = IntegerField(default=0)
    homepage4 = IntegerField(default=0)
    homepage5 = IntegerField(default=0)
    logins = IntegerField(default=0)

    class Meta:
        database = db