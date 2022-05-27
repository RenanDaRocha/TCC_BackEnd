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
            TRECHO2
        FROM CODIGOS
        WHERE DIFICULDADE = '{dificuldade}'
        ORDER BY DIFICULDADE, ID
        """
    , True)

def setCodigos():
    conexao = get_conexao()

    for item in request.json:
        TITULO      = item.get('TITULO')
        DESCRICAO   = item.get('DESCRICAO')
        RESPOSTA    = item.get('RESPOSTA')
        DIFICULDADE = item.get('DIFICULDADE')
        TRECHO1     = item.get('TRECHO1')
        TRECHO2     = item.get('TRECHO2')
        
        sql = f"""
            UPDATE OR INSERT INTO CODIGOS (
                TITULO,
                DESCRICAO,
                RESPOSTA,
                DIFICULDADE,
                TRECHO,
                TRECHO2
            ) VALUES (
                '{TITULO}',
                '{DESCRICAO}',
                '{RESPOSTA}',
                {DIFICULDADE},
                '{TRECHO1}'
                '{TRECHO2}'
            )
            MATCHING (ID)
        """

        conexao.execute_immediate(sql)

    conexao.commit()
    return "Códigos atualizados/inseridos com sucesso"