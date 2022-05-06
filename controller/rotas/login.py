from flask import request
from controller.fb_control import get_select_json
from controller.fb_control import get_conexao

def getLogin(login, senha):
    return get_select_json(
        f"""
        SELECT
            ID,
            NOME
        FROM LOGIN C
        WHERE LOGIN = '{login}' 
          AND SENHA = '{senha}'
        """
    , True)

def setLogin():
    conexao = get_conexao()

    for item in request.json:
        LOGIN = item.get('LOGIN')
        SENHA = item.get('SENHA')
        NOME  = item.get('NOME')
        
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