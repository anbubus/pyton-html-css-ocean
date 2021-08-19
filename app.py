import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash

# configuracao
DATABASE = "blog.db"
SECRET_KEY = "anbubu"

app = Flask(__name__)
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def antes_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def depois_request(exc):
    g.bd.close()

@app.route('/entradas')
def show_msg():
    return render_template('exibir_entradas.html')

#passa pra ele uma string que vai ser a url, e ele linkara ela com uma função de python
@app.route('/hello')
def inicial_page():
    return "Hello Word"