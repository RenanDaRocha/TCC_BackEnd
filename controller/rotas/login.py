from queue import Empty
from flask import request
from controller.fb_control import get_select_json
from controller.fb_control import get_conexao

def login():
    conexao = get_conexao()
    LOGIN   = request.json.get('LOGIN')
    SENHA   = request.json.get('SENHA')
    TRECHO  = ''

    if (SENHA):
        TRECHO = f"AND SENHA = '{SENHA}'"

    return get_select_json(
        f"""
        SELECT
            ID,
            LOGIN,
            SENHA,
            NOME,
            NIVEL,
            DISCIPLINA
        FROM USUARIO
        WHERE LOGIN = '{LOGIN}'
        {TRECHO}
        """
    , True)

def setUsuario():
    conexao = get_conexao()
    LOGIN      = request.json.get('LOGIN')
    SENHA      = request.json.get('SENHA')
    NOME       = request.json.get('NOME')
    NIVEL      = request.json.get('NIVEL')
    DISCIPLINA = request.json.get('DISCIPLINA')
        
    sql = f"""
        UPDATE OR INSERT INTO USUARIO (
            LOGIN,
            SENHA,
            NOME,
            NIVEL,
            DISCIPLINA
        ) VALUES (
            '{LOGIN}',
            '{SENHA}',
            '{NOME}',
            '{NIVEL}',
            '{DISCIPLINA}'
        )
        MATCHING (LOGIN)
    """

    conexao.execute_immediate(sql)

    conexao.commit()
    return "Login atualizados/inseridos com sucesso"