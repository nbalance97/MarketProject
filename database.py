import sqlite3

import click

from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            "Market.sqlite"
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def generate_sqlite():
    con = sqlite3.connect("Market.sqlite3")
    with open('Market.sql') as f:
        con.executescript(f.read())
    con.close()



