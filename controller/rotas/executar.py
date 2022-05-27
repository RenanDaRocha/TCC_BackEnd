import json
from flask import request
from controller.fb_control import get_select_json
from controller.fb_control import get_conexao

def executar(code, resposta):
    retorno = ''
    try:
        if eval(code) == eval(resposta):
            retorno = 'C'
        else:
            retorno = 'D'
    except:
        retorno= 'E'
    return (retorno)
    