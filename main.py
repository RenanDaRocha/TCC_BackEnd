from flask import Flask, request#, render_template, redirect, request, abort, jsonify, send_from_directory
from flask_cors import CORS
import os
# internos
from controller.rotas.login import login, setUsuario
from controller.rotas.codigos import getCodigos, getCodigosUsuario, setCodigos
from controller.rotas.concluido import getConcluido, getConcluidoAlunos, setConcluido
from controller.rotas.executar import executar

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=["POST"])
def Login():
    return login()

@app.route('/enviarusuario', methods=["POST"])
def set_Usuario():
    return setUsuario()

@app.route('/codigos/<dificuldade>')
def get_Codigos(dificuldade):
    return getCodigos(dificuldade)

@app.route('/codigosusuario/<usuario>')
def get_Codigos_Usuario(usuario):
    return getCodigosUsuario(usuario)

@app.route('/enviarcodigos', methods=["POST"])
def set_Codigos():
    return setCodigos()

@app.route('/concluido/<usuario>')
def get_Concluido(usuario):
    return getConcluido(usuario)

@app.route('/concluidoaluno/<codigo>/<usuario>')
def get_Concluido_Alunos(codigo, usuario):
    return getConcluidoAlunos(codigo, usuario)

@app.route('/enviarconcluido', methods=["POST"])
def set_Concluido():
    return setConcluido()

@app.route('/executar', methods=["POST"])
def Executar():
    return executar()

if __name__ == '__main__' : 
    port = int(os.environ.get('PORT',8080))
    app.run(host='0.0.0.0', port=port)