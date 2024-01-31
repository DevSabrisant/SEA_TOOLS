from flask import Flask
from Seatools.extensions import Configurations
from Seatools.blueprints.views import Telas

app = Flask(__name__)
Configurations.init_app(app)
app.register_blueprint(Telas)

if __name__ == "__main__":
   app.run(debug=True)