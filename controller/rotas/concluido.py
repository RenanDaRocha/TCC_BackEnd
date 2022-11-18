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

def getConcluidoRanking():
    return get_select_json(
        f"""
        SELECT
            U.NOME,
            R.CADTOTALRESOL AS TOTAL,
            R.CADTOTAL1RESOL AS FACIL,
            R.CADTOTAL2RESOL AS MEDIO,
            R.CADTOTAL3RESOL AS DIFICIL
        FROM USUARIO U
        LEFT JOIN RESOLVIDOS(U.ID) R ON (0=0)
        WHERE R.CADTOTALRESOL > 0
        ORDER BY TOTAL DESC, R.ULTIMO
        """
    , True) 

def getConcluidoRankingPonto():
    return get_select_json(
        f"""
        SELECT
            U.NOME,
            R.PONTOSTOTAL AS TOTAL,
            R.PONTOSFACIL AS FACIL,
            R.PONTOSMEDIO AS MEDIO,
            R.PONTOSDIFICIL AS DIFICIL
        FROM USUARIO U
        LEFT JOIN RESOLVIDOS(U.ID) R ON (0=0)
        WHERE R.CADTOTALRESOL > 0
        ORDER BY TOTAL DESC, R.ULTIMO
        """
    , True) 

def getConcluidoAlunos(codigo, usuario):

    return get_select_json(
        f"""
        SELECT
            U.NOME,
            CC.DATA
        FROM CONCLUIDOS CC
        LEFT JOIN CODIGOS CD ON (CD.ID = CC.ID_CODIGO)
        LEFT JOIN USUARIO U ON (U.ID = CC.ID_USUARIO)
        WHERE CD.ID = ({codigo})
          AND CD.ID_USUARIO = ({usuario})
        """
    , True)

def setConcluido():
    conexao = get_conexao()

    ID_USUARIO = request.json.get('ID_USUARIO')
    ID_CODIGO  = request.json.get('ID_CODIGO')
    PONTO      = request.json.get('PONTO')
        
    conexao.execute_immediate(f"execute procedure SP_CODIGOCONCLUIDO({ID_USUARIO},{ID_CODIGO},{PONTO})")
    conexao.commit()
    return "Concluido atualizados/inseridos com sucesso"