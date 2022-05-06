from flask import request
from controller.fb_control import get_select_json
from controller.fb_control import get_conexao

def getCodigos():
    return get_select_json(
        """
        SELECT
            ID,
            DESCRICAO,
            RESPOSTA,
            DIFICULDADE
        FROM CODIGOS
        ORDER BY DIFICULDADE, ID
        """
    , True)

def setCodigos():
    conexao = get_conexao()

    for item in request.json:
        DESCRICAO   = item.get('DESCRICAO')
        RESPOSTA    = item.get('RESPOSTA')
        DIFICULDADE = item.get('DIFICULDADE')
        
        sql = f"""
            UPDATE OR INSERT INTO CONTAS (
                DESCRICAO,
                RESPOSTA,
                DIFICULDADE
            ) VALUES (
                '{DESCRICAO}',
                '{RESPOSTA}',
                {DIFICULDADE}
            )
            MATCHING (ID)
        """

        conexao.execute_immediate(sql)

    conexao.commit()
    return "Códigos atualizados/inseridos com sucesso"