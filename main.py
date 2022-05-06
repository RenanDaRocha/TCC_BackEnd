from flask import Flask, request#, render_template, redirect, request, abort, jsonify, send_from_directory
from flask_cors import CORS
import os
# internos
from controller.rotas.login import getLogin, setLogin
from controller.rotas.codigos import getCodigos, setCodigos
from controller.rotas.concluido import getConcluido, setConcluido

app = Flask(__name__)
CORS(app)

@app.route('/login/<login>/<senha>')
def get_Login(login, senha):
    return getLogin(login, senha)

@app.route('/enviarlogin', methods=["POST"])
def set_Login():
    return setLogin()


@app.route('/codigos')
def get_Codigos():
    return getCodigos()

@app.route('/enviarcodigos', methods=["POST"])
def set_Codigos():
    return setCodigos()


@app.route('/concluido/<usuario>/<codigo>')
def get_Concluido(usuario, codigo):
    return getConcluido(usuario, codigo)

@app.route('/enviarconcluido', methods=["POST"])
def set_Concluido():
    return setConcluido()

if __name__ == '__main__' : 
    port = int(os.environ.get('PORT',8090))
    app.run(host='0.0.0.0', port=port)
