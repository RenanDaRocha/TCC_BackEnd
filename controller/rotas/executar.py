import subprocess
from sre_compile import isstring
from flask import request
from controller.fb_control import get_select_json
from controller.fb_control import get_conexao

def executar():
    CODIGO     = request.json.get('CODIGO')
    RESPOSTA   = request.json.get('RESPOSTA')
    ID_USUARIO = request.json.get('ID_USUARIO')
    RETORNO = ''
    EXECUTAR = f"""
from sre_compile import isstring
import usuario_{ID_USUARIO} 

resposta = usuario_{ID_USUARIO}.main()
arquivo = open("codigos/resposta_{ID_USUARIO}.txt", "w")
if isstring(resposta):
    arquivo.write(resposta)
else:
    arquivo.write(str(resposta))    
    """
    
    try:
        arquivoE = open(f"codigos/executar_{ID_USUARIO}.py", "w")
        arquivoC = open(f"codigos/usuario_{ID_USUARIO}.py", "w")
        arquivoE.writelines(EXECUTAR)
        arquivoC.writelines(CODIGO)
        arquivoE.close()
        arquivoC.close()
        subprocess.call(['py', f"codigos/executar_{ID_USUARIO}.py"])

        arquivoResp = open(f"codigos/resposta_{ID_USUARIO}.txt", "r")
        if RESPOSTA == arquivoResp.readlines()[0]:
            RETORNO = 'V'
        else:
            RETORNO = 'F'          
    except:
        RETORNO= 'ERRO'
    return (RETORNO)
    