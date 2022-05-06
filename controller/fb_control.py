import fdb
from controller.json_control import jsonTexto

def get_conexao():
    try:
        return fdb.connect(
            host="127.0.0.1",
            port=3053,
            database="C:\SGW\Dados\ArribaMobile\BANCO.FDB",
            user="SYSDBA",
            password="masterkey"
        )
    except:
        print('Falha ao efetuar a conexão com o banco de dados')
        return None

def set_fim_conexao(query):
    query.close()
    query.connection.close()

def get_query(sql):
    conexao = get_conexao()
    query = conexao.cursor()   
    return query.execute(sql)

def get_select_sem_nomes(sql):
    query = get_query(sql)    
    resultado = query.fetchall()
    set_fim_conexao(query)
    return resultado

def get_select_com_nomes(sql):      
    resultado = []
    query = get_query(sql)    
    for registro in query.fetchall():
        item = { description[0]: registro[col] for col, description in enumerate(query.description) }
        resultado.append(item)
    return resultado

def get_select(sql, com_nomes=True):
    if (com_nomes):
        return get_select_com_nomes(sql)
    else:
        return get_select_sem_nomes(sql)

def get_select_json(sql, com_nomes=True):
    return jsonTexto(get_select(sql,com_nomes))

