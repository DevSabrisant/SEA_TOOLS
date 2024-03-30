from blueprints.views import Telas
from database.database import db
from database.models.acess import User
from database.models.dash import Dash


def configura_all(app):
    configure_viewes(app)
    configure_db()

def configure_viewes(app):
    app.register_blueprint(Telas)

def configure_db():
    db.connect()
    db.create_tables([Dash, User])

