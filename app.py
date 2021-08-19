import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash

# configuracao
DATABASE = "blog.db"
SECRET_KEY = "anbubu"

app = Flask(__name__)
app.config.from_object(__name__)

def conect_db():
    return sqlite3.connect(app.confg['DATABASE'])

@app.before_request
def before_req():
    g.db = conect_db()

@app.teardown_request
def after_req():
    g.db.close()

#passa pra ele uma string que vai ser a url, e ele linkara ela com uma função de python
@app.route('/hello')
def inicial_page():
    return "Hello Word"