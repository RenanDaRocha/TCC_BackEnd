from flask import request
from controller.fb_control import get_select_json
from controller.fb_control import get_conexao

def getLogin():
    return get_select_json(
        """
        SELECT
            ID,
            LOGIN, 
            SENHA,
            NOME
        FROM LOGIN
        """
    , True)

def setLogin():
    conexao = get_conexao()
    LOGIN = request.json.get('LOGIN')
    SENHA = request.json.get('SENHA')
    NOME  = request.json.get('NOME')
        
    sql = f"""
        UPDATE OR INSERT INTO LOGIN (
            LOGIN,
            SENHA,
            NOME
        ) VALUES (
            '{LOGIN}',
            '{SENHA}',
            '{NOME}'
        )
        MATCHING (LOGIN)
    """

    conexao.execute_immediate(sql)

    conexao.commit()
    return "Login atualizados/inseridos com sucesso"