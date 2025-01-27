import psycopg2
from Utils.Respuestas import Respuesta
from Utils.Decoders import RequestDecoder
#from db import Acceso
from flask import Blueprint, request, jsonify
#from flask_jwt_extended import jwt_required
import json
from Utils.CallOpenAI import OpenAIConector
genera_bp = Blueprint('pregunta', __name__)

@genera_bp.route('', methods=['POST'])
#@jwt_required()
def ObtieneCodigo():
    try:
        #Valida el json de entrada
        params = request.get_json()
        pregunta = params.get('pregunta')
        if pregunta == None:
            raise Exception("Entrada de datos incorrecta.")
        
        pregunta_ia = f"{pregunta.capitalize()}, por favor devuelveme solo el código generado, no hagas un resumen"
        IniciaOAI = OpenAIConector()
        RespuestaOAI = IniciaOAI.enviarOPENAI(pregunta_ia)

        if RespuestaOAI != '':
            Response = {'Exito': True, 'Resultado': RespuestaOAI, 'Detalle': ''}
        else:
            Response = {'Exito': False, 'Resultado': 'No se obtuvieron resultados.', 'Detalle': ''}
        
    except Exception as e:
        Response = {'Exito': False, 'Resultado': 'Error al generar la consulta.', 'Detalle': str(e)}
    
    return jsonify(Response)