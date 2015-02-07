import datetime
import random
import sys

from flask import Flask, render_template, redirect, url_for
from flask.ext.script import Manager


# Globals
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asd'
app.config['DEBUG'] = True

# Misc stuff
def random_caps(s):
    r = ''
    for c in s:
        if int(2 * random.random()) is 0:
            r += c.capitalize()
        else:
            r += c
    return r

def megahertz():
    return 100 * random.random()

def yomyman_style():
    styles = ['cachou', 'jambon', 'epinard', 'lasagne', 'haricot', 'sandwich']
    return 'cool-style-' + styles[int(random.random() * len(styles))]

def logo_alternate():
    base_path = '/static/img/logo-alternate-300/'
    images = [
        '50-bacon-50-biere-50-camembert.png',
        'dj-jean-michel-mc-pierre-gustave.jpg',
        'i-love-chips.jpg',
        'le-passe-c-etait-mieux-avant.jpg',
        'c-est-vachement-cool.jpg',
        'arc-en-le-ciel.jpg',
        'aspiration.jpg',
        'boules.jpg',
        'etoile.jpg',
        'megas-pixels.jpg',
        'petits-pixels.jpg',
        'pochette-camembert.jpg',
        'pouce.jpg',
        'trim.jpg',
        'trop-de-la-balle.jpg',
    ]
    return base_path + images[int(random.random() * len(images))]

def mot_du_jour():
    day = int(datetime.datetime.now().strftime('%d'))
    mots_du_jour = [
        'une gomme', 'une pomme', 'phazms', '08 36 65 65 65', 'le mot du jour',
        'cool', 'trop de la balle', 'coucou', 'salut les copains',
        'un sandwich', 'caribou', 'jus', 'du pate', 'poney', 'castor',
        'cancun', 'hula hoop', 'criterium', 'lampadaire', 'tabernacle',
        'anticonstitutionnellement', 'grut', 'i feel good', 'cumulonumbus',
        'chewing gum', 'jericane', 'malaxer', 'competant', 'moineau', 'wesh',
        'platane', 'sycomore', 'blaireau', 'perudo', 'azymute',
        'moissoneuse batteuse', 'tracteur', 'pudding', '1000 pates', '42',
        'centipede',
    ]
    return random_caps(mots_du_jour[day % len(mots_du_jour)])

def mot_debile_qui_se_mange():
    mots_debiles = [
        'beurre', 'lait', 'yahourt', 'pain', 'gruyere', 'margarine',
        'curcumin', 'd\'epinard', 'banane', 'salade', 'brioche',
        'sucre', 'chips', 'laitage', 'lukum', 'flotte', 'chupa-chups',
        'yogourt',
    ]
    return mots_debiles[int(random.random() * len(mots_debiles))]

app.jinja_env.globals.update(
    yomyman_style=yomyman_style,
    logo_alternate=logo_alternate,
    mot_du_jour=mot_du_jour,
    megahertz=megahertz,
    mot_debile_qui_se_mange=mot_debile_qui_se_mange,
)

def get_hackz():
    hackz_list = []
    hackz_list.append({
        'title': '3615 Cryptage',
        'img': '/static/img/hackz/3615cryptage/logo.jpg',
        'url': url_for('hackz_3615cryptage'),
    })
    hackz_list.append({
        'title': 'Calculatrice.exe',
        'img': '/static/img/hackz/calculatrice/logo.jpg',
        'url': url_for('hackz_calculatrice'),
    })
    random.shuffle(hackz_list)
    return hackz_list

# Routes
@app.route('/')
def home():
    images = get_hackz()
    return render_template('home.html', images=images)

@app.route('/hackz/3615cryptage')
def hackz_3615cryptage():
    return render_template('hackz/3615cryptage.html')

@app.route('/hackz/calculatrice.exe')
def hackz_calculatrice():
    return render_template('hackz/calculatrice.html')

# Main
if __name__ == "__main__":
    manager = Manager(app)
    manager.run()
