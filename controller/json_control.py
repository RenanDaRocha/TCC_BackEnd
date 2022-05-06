import json
import datetime

def jsonFiltrar(jsonObj, campo, valor):
    #return list(filter(lambda value: value[campo] == valor, jsonObj))
    return list(filter(lambda value: str(value[campo]) == str(valor), jsonObj))

def jsonFiltrarParcial(jsonObj, campo, valor):
    #return list(filter(lambda value: value[campo] == valor, jsonObj))
    return list(filter(lambda value: str(valor).upper() in str(value[campo]).upper(), jsonObj))

def jsonTexto(jsonObj):

    def parseFormat(item):
        if isinstance(item, (datetime.date, datetime.datetime)):
            return item.isoformat()            

    return json.dumps(jsonObj, ensure_ascii=False, indent=4, default=parseFormat).encode("utf-8")