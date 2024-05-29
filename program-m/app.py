from flask import Flask
from Api.api import blueprint_api
from kino.kino import init_app
from model import Rezervace, db

# inicializace aplikace flask
app = Flask(__name__)

# nastaveni uri pro pripojeni k sqlite databazi
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kinosal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'abc'

# registrace modulu api
app.register_blueprint(blueprint_api)
# inicializace modulu kinosal
init_app(app)

# spusteni aplikace v rezimu debug na portu 8001
if __name__ == '__main__':
    app.run(debug=True, port=8001)