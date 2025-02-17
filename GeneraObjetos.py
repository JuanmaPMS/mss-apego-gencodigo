from Utils.Respuestas import Respuesta
from Utils.Decoders import RequestDecoder
from flask import Blueprint, request, jsonify,Response,send_file
from Utils.CallOpenAI import OpenAIConector
from db import Acceso
from getscript import Obtener
from ExecOpenAI import Exec
from draw import ER
from io import BytesIO

generaObjetos_bp = Blueprint('genObjetos', __name__)

@generaObjetos_bp.route('/Esquemas', methods=['GET'])
def ObtieneEsquema():
    columnas = ['schema_name']
    pregunta_data = Acceso("information_schema.schemata").EjecutaVista(columnas=columnas)   
    return jsonify(pregunta_data)  
  
@generaObjetos_bp.route('/Tablas/<Esquema>', methods=['GET'])
def ObtieneTablas(Esquema:str):
    columnas = ['tablename']
    condiciones_Anexo = {
        'schemaname': ('=', Esquema)
        }
    pregunta_data = Acceso("pg_catalog.pg_tables").EjecutaVista(columnas=columnas, condiciones=condiciones_Anexo)  
    lista_cadenas = [diccionario['tablename'] for diccionario in pregunta_data] 
    return jsonify(lista_cadenas) 

@generaObjetos_bp.route('/Script/<tabla>', methods=['GET'])
def GenTablas(tabla:str):
    ScriptResponse = Obtener.GetScript(tabla)
    ScriptResponse = Exec().enviarOPENAIRefinaQuery(ScriptResponse).replace('```sql','').replace('```','')
    return jsonify({"ScriptTable":ScriptResponse}) 

@generaObjetos_bp.route('/ejecuta', methods=['POST'])
def Executequery():
    datos = request.get_json()
    query = datos.get('query')
    ScriptResponse = Acceso('').EjecutaRaw(query)
    return jsonify(ScriptResponse) 

@generaObjetos_bp.route('/Persiste', methods=['POST'])
def ExecutequeryPersiste():
    datos = request.get_json()
    query = datos.get('query')
    ScriptResponse = Acceso('').EjecutaRaw(query)
    return jsonify(ScriptResponse) 

@generaObjetos_bp.route('/Gen', methods=['POST'])
def RealizaPregunta():
    datos = request.get_json()
    Tablas = datos.get('tablas')
    Pregunta = datos.get('Pregunta')
    Response = Exec.enviarOPENAI(Tablas, Pregunta)
    return jsonify({"script": Response.replace('```sql','').replace('```','')}) 

@generaObjetos_bp.route('/ER', methods=['GET'])
def GenER():
    image_bytes = ER.creaER() 
    image_stream = BytesIO(image_bytes)
    return send_file(image_stream, mimetype='image/png')




