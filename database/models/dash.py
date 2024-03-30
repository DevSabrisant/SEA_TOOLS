from peewee import Model, IntegerField, CharField
from database.database import db

class Dash(Model):

    titulo = CharField()
    homepage = IntegerField()
    homepage2 = IntegerField()
    homepage3 = IntegerField()
    homepage4 = IntegerField()
    homepage5 = IntegerField()
    logins = IntegerField()

    class Meta:
        database = db