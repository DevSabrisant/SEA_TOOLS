from flask import Flask
from configurations import configura_all
import secrets

app = Flask(__name__)
configura_all(app)
app.secret_key = secrets.token_hex(16)


if __name__ == "__main__":
    app.run()


