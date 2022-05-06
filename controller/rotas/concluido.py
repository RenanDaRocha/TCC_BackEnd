from flask import request
from controller.fb_control import get_select_json
from controller.fb_control import get_conexao

def getConcluido(usuario, codigo):

    return get_select_json(
        f"""
        SELECT 
            DATA
        FROM CONCLUIDO
        WHERE ID_USUARIO = '{usuario}'
          AND ID_CODIGO = '{codigo}'
        """
    , True)

def setConcluido():
    conexao = get_conexao()

    for item in request.json:
        ID_USUARIO = item.get('ID_USUARIO')
        ID_CODIGO  = item.get('ID_CODIGO')
        DATA       = item.get('DATA')
        
        sql = f"""
            UPDATE OR INSERT INTO CONCLUIDO (
                ID_USUARIO,
                ID_CODIGO,
                DATA
            ) VALUES (
                {ID_USUARIO},
                {ID_CODIGO},
                {DATA}
            )
            MATCHING (ID_USUARIO, ID_CODIGO)
        """

        conexao.execute_immediate(sql)

    conexao.commit()
    return "Concluido atualizados/inseridos com sucesso"