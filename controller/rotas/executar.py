import json
from flask import request
from controller.fb_control import get_select_json
from controller.fb_control import get_conexao

def executar():
    print('foi')
    CODIGO = request.json.get('CODIGO')
    RESPOSTA = request.json.get('RESPOSTA')
    RETORNO = ''
    print(CODIGO)
    print(RESPOSTA)

    try:
        if eval(CODIGO) == eval(RESPOSTA):
            RETORNO = 'C'
        else:
            RETORNO = 'D'
    except:
        RETORNO= 'E'
    print(RETORNO)
    return (RETORNO)
    