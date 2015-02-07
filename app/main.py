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

def mot_cool():
    mots_cools = [
        'cool', 'sympa', 'gentil', 'genial', 'excellent', 'superbe', 'super',
        'vraiment tres bien', 'bien', 'qui en a dans le pantalon', 'top',
    ]
    return mots_cools[int(random.random() * len(mots_cools))]

def mot_pascool():
    return 'pas tres ' + mot_cool()

app.jinja_env.globals.update(
    yomyman_style=yomyman_style,
    logo_alternate=logo_alternate,
    mot_du_jour=mot_du_jour,
    megahertz=megahertz,
    mot_debile_qui_se_mange=mot_debile_qui_se_mange,
    mot_cool=mot_cool,
    mot_pascool=mot_pascool,
)

# Helpers
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

def get_copaings():
    copaings_list = []
    copaings_list.append({
        'title': 'm1ch3l',
        'description': 'm1ch3l est cool, m1ch3l aime les gommes.',
        'img': '/static/img/copaings/m1ch3l.jpg',
        'links': [
            {'url': 'http://m1ch3l.biz/', 'title': 'Le site de m1ch3l'},
            {'url': 'http://radio.m1ch3l.biz/', 'title': 'Radio m1ch3l'},
        ],
    })
    copaings_list.append({
        'title': 'salut c\'est cool',
        'img': '/static/img/copaings/scc.jpg',
        'description': '<3<3<3<3',
        'links': [
            {'url': 'http://salutcestcool.com',
             'title': 'Le site de salut c\'est cool'},
            {'url': 'http://facebook.com/salutcestcool',
             'title': 'Facebook'},
        ],
    })
    copaings_list.append({
        'title': 'Gars Cool',
        'img': '/static/img/copaings/garscool.jpg',
        'description': 'cool',
        'links': [
            {'url': 'https://www.facebook.com/garscool',
             'title': 'Facebook'},
            {'url': 'http://garscool.tumblr.com',
             'title': 'Tumblr'},
            {'url': 'https://twitter.com/garscool',
             'title': 'Twitter'},
        ],
    })
    copaings_list.append({
        'title': 'C\'est moi',
        'img': '/static/img/copaings/cestmoi.jpg',
        'description': 'hihi',
        'links': [
            {'url': 'https://www.facebook.com/cestmoi42',
             'title': 'Facebook de C\'est moi'}
        ],
    })
    copaings_list.append({
        'title': 'Furrtek',
        'img': '/static/img/copaings/furrtek.png',
        'description': 'Avant on se faisait electrocuter, maintenant on peut se faire electroniquer',
        'links': [
            {'url': 'http://furrtek.free.fr',
             'title': 'Site officiel'},
            {'url': 'https://www.youtube.com/user/furrtek/videos',
             'title': 'Youtube'}
        ],
    })
    copaings_list.append({
        'title': 'sbrk.org',
        'img': '/static/img/copaings/sbrk.jpg',
        'description': mot_cool(),
        'links': [
            {'url': 'http://sbrk.org',
             'title': 'Sbrk'},
            {'url': 'http://mxs.sbrk.org',
             'title': 'mxs'},
        ]
    })
    copaings_list.append({
        'title': 'Le club de Gym',
        'img': '/static/img/copaings/club.jpg',
        'description': 'Collectif d\'artistes et de muscles',
        'links': [
            {'url': 'https://www.facebook.com/legymclub',
             'title': 'Facebook'}
        ]
    })
    copaings_list.append({
        'title': 'Leonard Gordon Alain Souchon de la Gomme du Camembert',
        'img': '/static/img/copaings/leonard.jpg',
        'description': 'Waf',
        'links': [
            {'url': 'https://www.facebook.com/leonard.gomme',
             'title': 'Facebook'},
            {'url': 'http://leonard-camembert.tumblr.com',
             'title': 'Tumblr'},
        ]
    })
    copaings_list.append({
        'title': 'Je suis pas un monstre !',
        'img': '/static/img/copaings/sassou-behance.jpg',
        'description': 'par Sassou Youpi',
        'links': [
            {'url': 'https://www.behance.net/sassouyoupi', 'title': 'Behance'}
        ]
    })
    copaings_list.append({
        'title': 'Vadim',
        'img': '/static/img/copaings/apokorunta.png',
        'description': '',
        'links': [
            {'url': 'http://apokorunta.free.fr/blog/index.php',
             'title': 'Apokorunta'},
        ]
    })
    for copaing in copaings_list:
        if 'img' not in copaing:
            copaing['img'] = '/static/img/img-not-found-400.png'
    random.shuffle(copaings_list)
    return copaings_list

# Routes
@app.route('/')
def home():
    images = get_hackz()
    images += get_copaings()
    return render_template('home.html', images=images)

@app.route('/hackz/3615cryptage')
def hackz_3615cryptage():
    return render_template('hackz/3615cryptage.html')

@app.route('/hackz/calculatrice.exe')
def hackz_calculatrice():
    return render_template('hackz/calculatrice.html')

@app.route('/hackz')
def hackz():
    hackzers = []
    return render_template('hackz.html', hackz=get_hackz(),
                           hackzers=hackzers)

@app.route('/copaings')
def copaings():
    return render_template('copaings.html', copaings=get_copaings())

# Main
if __name__ == "__main__":
    manager = Manager(app)
    manager.run()
