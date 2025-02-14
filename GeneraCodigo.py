import base64
import io
import os
import psycopg2
from Utils.Respuestas import Respuesta
from Utils.Decoders import RequestDecoder
#from db import Acceso
from flask import Blueprint, request, jsonify, send_file
#from flask_jwt_extended import jwt_required
import json
from Utils.CallOpenAI import OpenAIConector
from Utils.ManejoCadenas import Cadenas
from db import Acceso
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
        
        #pregunta_ia = f"{pregunta.capitalize()}, por favor devuelveme solo el código generado en texto plano, no hagas un resumen y tampoco generes comentarios ni etiquetas"
        #pregunta_ia = f"{pregunta.capitalize()}, el codigo que generes devuelvelo identado en un objeto json dentro de la propiedad llamada codigo y tambien contendra un propiedad llamada explicacion con la explicacion del codigo que generaste , no hagas un resumen y tampoco generes comentarios ni etiquetas"
        pregunta_ia = f"de este texto '{pregunta.capitalize()}' generame el código y lo regresaras en un objeto json en un solo nodo que contendra dos propiedades una llamada codigo en el cual su valor sera la respuesta que  generes y la otra propiedad se llamara explicacion que tendra el valor de la explicacion del codigo, no hagas un resumen y tampoco generes comentarios ni etiquetas "
        IniciaOAI = OpenAIConector()
        RespuestaOAI = IniciaOAI.enviarOPENAI(pregunta_ia)
        cadena= Cadenas()
        if RespuestaOAI != '':
            #Response = {'Exito': True, 'Resultado': cadena.eliminar_lineas( RespuestaOAI), 'Detalle': ''}
            Response = {'Exito': True, 'Resultado':  RespuestaOAI, 'Detalle': ''}
        else:
            Response = {'Exito': False, 'Resultado': 'No se obtuvieron resultados.', 'Detalle': ''}
        
    except Exception as e:
        Response = {'Exito': False, 'Resultado': 'Error al generar la consulta.', 'Detalle': str(e)}
    
    return jsonify(Response)

@genera_bp.route('/descarga', methods=['POST'])
def DescargaArchivo():
    try:
        
        # Obtener datos del request
        data = request.json
        code = data.get("code")
        
        pregunta_ia = f"Del siguiente codigo: {code} solo devuelveme  la extensión del tipo de archivo que le corresponde de acuerdo al lenguaje en el que esta escrito el código y no hagas resumen ni comentarios."
        extension = OpenAIConector().enviarOPENAI(pregunta_ia)

        # Validar que se proporcionaron los datos necesarios
        if not code or not extension:
            return {"error": "Faltan datos. Se requiere 'code' y 'extension'."}, 400

        # Crear el archivo en memoria
        file_stream = io.BytesIO()
        file_stream.write(code.encode('utf-8'))
        file_stream.seek(0)

        # Nombre del archivo a devolver
        filename = f"codigo_generado{extension}"
        
        base64_encoded = base64.b64encode(file_stream.read()).decode('utf-8')
        return jsonify({"Exito": True, "Detalle": base64_encoded, "Resultado": filename})

    except Exception as e:
        return {"error": str(e)}, 500
    
@genera_bp.route('/titulo', methods=['POST'])
#@jwt_required()
def ObtieneTitulo():
    try:
        #Valida el json de entrada
        params = request.get_json()
        descripcion = params.get('descripcion')
        if descripcion == None:
            raise Exception("Entrada de datos incorrecta.")
        
        condicionesPregunta = {
        'nombrecorto': ('=', "Titulo")
        }

     
        pregunta_data = Acceso("preguntasistema").EjecutaVista(condicionesPregunta)    
        pregunta = pregunta_data[0]["pregunta"]
        variables = pregunta_data[0]["variables"]
        pregunta_formulada = pregunta.replace(variables, descripcion)
        respuesta_openai = OpenAIConector().enviarOPENAI(pregunta_formulada)
        cadena = respuesta_openai.replace('json', '').split('```')[1].strip()
        titulojson = json.loads(cadena)
        titulo = titulojson["Titulo"]
             
        return jsonify({ "Exito" : True,
                    'Mensaje': 'Operación realizada con exito',
                    'Respuesta': titulo}), 200

    except (IndexError, json.JSONDecodeError) as e:
         return jsonify({"Exito" : False,
                    'Mensaje': "Ocurrio un error" ,
                    'Respuesta': str(e)}), 500
    except Exception as e:
        return jsonify({"Exito" : False,
                    'Mensaje': "Ocurrio un error" ,
                    'Respuesta': str(e)}), 500
        

        
      