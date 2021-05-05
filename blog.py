from flask import Flask
from flask import request
from flask import render_template

from datetime import date

import sqlite3
from sqlite3 import Error

blog = Flask(__name__)

@blog.route('/novotopico', methods=['GET', 'POST'])

def cadastro():
    if request.method == 'POST':
        topico = request.form['topico']

    return 'teste'

@blog.route('/teste', methods=['GET', 'POST'])

def ok():
    return render_template('teste.html')

@blog.route('/success')

def success():
    return render_template('success.html')

@blog.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404

blog.run()