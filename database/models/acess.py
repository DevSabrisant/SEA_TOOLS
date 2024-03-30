from peewee import Model, CharField
from database.database import db

class User(Model):
    username = CharField()
    password = CharField()
    permissions = CharField()

    class Meta:
        database = db