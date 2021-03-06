from flask import Flask, request#, render_template, redirect, request, abort, jsonify, send_from_directory
from flask_cors import CORS
import os
# internos
from controller.rotas.login import getLogin, setLogin
from controller.rotas.codigos import getCodigos, setCodigos
from controller.rotas.concluido import getConcluido, setConcluido
from controller.rotas.executar import executar

app = Flask(__name__)
CORS(app)

@app.route('/login')
def get_Login():
    return getLogin()

@app.route('/enviarlogin', methods=["POST"])
def set_Login():
    return setLogin()


@app.route('/codigos/<dificuldade>')
def get_Codigos(dificuldade):
    return getCodigos(dificuldade)

@app.route('/enviarcodigos', methods=["POST"])
def set_Codigos():
    return setCodigos()


@app.route('/concluido/<usuario>')
def get_Concluido(usuario):
    return getConcluido(usuario)

@app.route('/enviarconcluido', methods=["POST"])
def set_Concluido():
    return setConcluido()

@app.route('/executar/<code>/<resposta>')
def Executar(code, resposta):
    return executar(code, resposta)

if __name__ == '__main__' : 
    port = int(os.environ.get('PORT',8090))
    app.run(host='0.0.0.0', port=port)
