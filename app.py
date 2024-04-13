from flask import Flask
from configurations import configura_all
import secrets
#from blueprints.indisponibilidades import detalhes

app = Flask(__name__)
configura_all(app)
app.secret_key = secrets.token_hex(16)


if __name__ == "__main__":
    #print(detalhes('234567890'))
    app.run(debug=True)

