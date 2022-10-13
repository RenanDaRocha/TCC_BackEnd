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
    print(codigo)
    print(usuario)

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
        
    conexao.execute_immediate(f"execute procedure SP_CODIGOCONCLUIDO({ID_USUARIO},{ID_CODIGO})")
    conexao.commit()
    return "Concluido atualizados/inseridos com sucesso"