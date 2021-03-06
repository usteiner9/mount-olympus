"""
Mount Olympus web scraping example project for Real Python

https://realpython.com
"""
from datetime import datetime
import random

import bottle


@bottle.route('/')
def root():
    return bottle.redirect('/login')


@bottle.route('/login')
def login():
    return bottle.template('views/login.html')


@bottle.route('/login', method='POST')
def submit_login():
    username = bottle.request.forms.get('user')
    password = bottle.request.forms.get('pwd')
    if username == 'zeus' and password == 'ThunderDude':
        return bottle.redirect('/profiles')
    return bottle.template('views/login_failed.html')


@bottle.route('/static/<filepath:path>')
def serve_static(filepath):
    return bottle.static_file(filepath, root='static/')


@bottle.route('/profiles')
def profiles():
    return bottle.template('views/profiles.html')


@bottle.route('/profiles/aphrodite')
def aphrodite():
    return bottle.template('views/aphrodite.html')


@bottle.route('/profiles/poseidon')
def poseidon():
    return bottle.template('views/poseidon.html')


@bottle.route('/profiles/dionysus')
def dionysus():
    return bottle.template('views/dionysus.html')


@bottle.route('/dice')
def dice():
    result = random.randint(1, 6)
    time = datetime.now().strftime("%B %d, %Y %I:%M:%S%p")
    return bottle.template('views/dice.html', random=result, time=time)


app = bottle.default_app()
