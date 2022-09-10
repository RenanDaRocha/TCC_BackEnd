from flask import request
from controller.fb_control import get_select_json
from controller.fb_control import get_conexao

def getConcluido(usuario):

    return get_select_json(
        f"""
        SELECT 
            *
        FROM RESOLVIDOS({usuario})
        """
    , True)

def getConcluidoAlunos(codigo, usuario):

    return get_select_json(
        f"""
        SELECT
            L.NOME,
            CC.DATA
        FROM CONCLUIDOS CC
        LEFT JOIN CODIGOS CD ON (CD.ID = CC.ID_CODIGO)
        LEFT JOIN LOGIN L ON (L.ID = CC.ID_USUARIO)
        WHERE CD.ID = ({codigo})
          AND CD.ID_USUARIO = ({usuario})
        """
    , True)

def setConcluido():
    conexao = get_conexao()

    ID_USUARIO = request.json.get('ID_USUARIO')
    ID_CODIGO  = request.json.get('ID_CODIGO')
    DATA       = request.json.get('DATA')
        
    sql = f"""
        UPDATE OR INSERT INTO CONCLUIDOS (
            ID_USUARIO,
            ID_CODIGO,
            DATA
        ) VALUES (
            {ID_USUARIO},
            {ID_CODIGO},
            '{DATA}'
        )
        MATCHING (ID_USUARIO, ID_CODIGO)
    """

    conexao.execute_immediate(sql)

    conexao.commit()
    return "Concluido atualizados/inseridos com sucesso"