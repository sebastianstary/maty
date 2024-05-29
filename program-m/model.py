from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
class Rezervace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazevFilmu = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    typListku = db.Column(db.String(20), nullable=False)
    misto = db.Column(db.String(10), nullable=False)