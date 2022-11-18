from flask import request
from controller.fb_control import get_select_json
from controller.fb_control import get_conexao

def getCodigos(dificuldade):
    return get_select_json(
        f"""
        SELECT
            ID,
            TITULO,
            DESCRICAO,
            RESPOSTA,
            DIFICULDADE,
            TRECHO,
            TRECHO2,
            TEMPO1,
            TEMPO2,
            TEMPO3
        FROM CODIGOS
        WHERE DIFICULDADE = '{dificuldade}'
        ORDER BY DIFICULDADE, ID
        """
    , True)

def getCodigosUsuario(usuario):
    print(usuario)
    return get_select_json(
        f"""
        SELECT
            ID,
            TITULO,
            DESCRICAO,
            RESPOSTA,
            DIFICULDADE,
            TRECHO,
            TRECHO2,
            TEMPO1,
            TEMPO2,
            TEMPO3
        FROM CODIGOS
        WHERE ID_USUARIO = ({usuario})
        """
    , True)

def setCodigos():
    conexao = get_conexao()
    print(request.json)
    TITULO      = request.json.get('TITULO')
    DESCRICAO   = request.json.get('DESCRICAO')
    RESPOSTA    = request.json.get('RESPOSTA')
    DIFICULDADE = request.json.get('DIFICULDADE')
    TRECHO1     = request.json.get('TRECHO1')
    TRECHO2     = request.json.get('TRECHO2')
    ID_USUARIO     = request.json.get('USUARIO')
    TEMPO1     = request.json.get('TEMPO1')
    TEMPO2     = request.json.get('TEMPO2')
    TEMPO3     = request.json.get('TEMPO3')
    
    sql = f"""
        UPDATE OR INSERT INTO CODIGOS (
            TITULO,
            DESCRICAO,
            RESPOSTA,
            DIFICULDADE,
            TRECHO,
            TRECHO2,
            ID_USUARIO,
            TEMPO1,
            TEMPO2,
            TEMPO3
        ) VALUES (
            '{TITULO}',
            '{DESCRICAO}',
            '{RESPOSTA}',
            {DIFICULDADE},
            '{TRECHO1}',
            '{TRECHO2}',
            {ID_USUARIO},
            {TEMPO1},
            {TEMPO2},
            {TEMPO3}
        )
        MATCHING (TITULO, ID_USUARIO)
    """
    
    conexao.execute_immediate(sql)

    conexao.commit()
    return "Códigos atualizados/inseridos com sucesso"