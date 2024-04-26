from database.database import db
from peewee import CharField, BlobField, Model, BooleanField,TextField


class Indisponibilidade(Model):
    protocolo = CharField(primary_key=True, unique=True)
    nomes_clientes = TextField(null=True)
    codigos_clientes = TextField(null=True)
    cto_clientes = TextField(null=True)
    foto = BlobField(null=True)
    cidade = CharField(null=True)
    status = BooleanField()
    nome_arquivo = TextField(null=True)

    class Meta:
        database = db