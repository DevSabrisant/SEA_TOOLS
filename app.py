from flask import Flask
from blueprints.views import Telas
import secrets


app = Flask(__name__)
app.register_blueprint(Telas)
app.secret_key = secrets.token_hex(16)

if __name__ == "__main__":
   app.run(debug=True)