# import modulů a funkcí
from flask import Flask, Blueprint, render_template, jsonify, request, redirect, url_for
from Api.api import GetDetailFilm, GetFilmy
from flask_sqlalchemy import SQLAlchemy
from model import Rezervace, db
import requests, json

# vytvoření blueprintu pro část aplikace
blueprint_kino = Blueprint('blueprint_kino', __name__,
    template_folder= 'templates',
    static_folder= 'static')

# inicializace databáze
def init_kino(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

# inicializace aplikace
def init_app(app):
    app.register_blueprint(blueprint_kino)
    init_kino(app)

# hlavni stranka
@blueprint_kino.route('/')
def hlavni_stranka():
    return render_template('kino/index.html')

# zobrazení seznamu filmů
@blueprint_kino.route('/filmy')
def filmy():
    data = GetFilmy()
    l = len(data) 
    return render_template('kino/filmy.html', filmy = data, length = l)

# zobrazení detailu filmu
@blueprint_kino.route('/<string:id>')
def detailFilmu(id):
    data = GetDetailFilm(id)
    return render_template('kino/detail.html', id=id, film=data)

# rezervace sedadel
@blueprint_kino.route('/odeslano', methods=['GET', 'POST'])
def formular():
    if request.method == 'POST':
        email = request.form['email']
        cislo_sedadla = request.form['sedadlo']
        film = request.form['nazev']
        listek = request.form['listek']
        rezerve = Rezervace(nazevFilmu=film, email=email, typListku=listek, misto=cislo_sedadla)
        db.session.add(rezerve)
        db.session.commit()
        return redirect(url_for('blueprint_kino.hlavni_stranka', success=True))
    else:
        return render_template('blueprint_kino.hlavni_stranka', success=False)

# získání rezervovaných sedadel
#@blueprint_kino.route('/zabrane_mista/<title>')
#def rezervovana_sedadla(title):
 #   misto_rezervovane = Rezervace.query.filter_by(nazevFilmu=title).all()
 #   mista = [rezervace.misto for rezervace in misto_rezervovane]
  #  return jsonify(mista)