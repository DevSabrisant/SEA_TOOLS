from database.database import db
from peewee import CharField, BlobField, Model, BooleanField


class Indisponibilidade(Model):
    protocolo = CharField(primary_key=True, unique=True)
    nomes_clientes = CharField(null=True)
    codigos_clientes = CharField(null=True)
    cto_clientes = CharField(null=True)
    foto = BlobField(null=True)
    cidade = CharField(null=True)
    status = BooleanField()
    nome_arquivo = CharField(null=True)

    class Meta:
        database = db