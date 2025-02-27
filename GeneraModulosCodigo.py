from flask import Flask, jsonify, request
from db import Acceso
from flask import Blueprint
from flask_jwt_extended import jwt_required

from decouple import config

from Utils.CallOpenAI import OpenAIConector
import json

modulosrepo_bp = Blueprint('modulosrepositorio', __name__)


@modulosrepo_bp.route('modulo',methods=['POST'])
#@jwt_required()
def CreateModulo():
    datos = request.get_json()
    #id= str(datos.get('id'))
    idproyectorepositorio= str(datos.get('idproyectorepositorio'))
    idusuario = str(datos.get('idusuario'))
    modulo = datos.get('modulo')
    dia = datos.get('dia')
    operacion = 'CREATE'
    params = [operacion, None, int(idproyectorepositorio), int(idusuario), modulo, dia]
    result = Acceso("fncrudrepositoriomodulos",params).EjecutaFuncionCRUD()
    
    if result:
            return jsonify({
                'Exito': result[0]["exito"],
                'Mensaje': result[0]["mensaje"],
                'Respuesta': result[0]["respuesta"]
            })
    else:
        return jsonify({'error': 'No se obtuvo respuesta de la base de datos.'}), 500

@modulosrepo_bp.route('modulo',methods=['PUT']) 
def UpdateModulo():
    datos = request.get_json()
    id= str(datos.get('id'))
    idusuario = str(datos.get('idusuario'))
    modulo = datos.get('modulo')
    operacion = 'UPDATE'
    params = [operacion, int(id), None, int(idusuario), modulo, None]
    result = Acceso("fncrudrepositoriomodulos",params).EjecutaFuncionCRUD()
        
    if result:
            return jsonify({
                'Exito': result[0]["exito"],
                'Mensaje': result[0]["mensaje"],
                'Respuesta': result[0]["respuesta"]
            })
    else:
        return jsonify({'error': 'No se obtuvo respuesta de la base de datos.'}), 500


@modulosrepo_bp.route('modulo/consultar',methods=['POST']) 
def ReadModuloId():
    datos = request.get_json()
    idusuario = str(datos.get('idusuario'))
    idproyectorepositorio= str(datos.get('idproyectorepositorio'))
    dia = datos.get('dia')
    operacion = 'READIDREPOSITORIO'
    params = [operacion, None, int(idproyectorepositorio), idusuario,  None, dia]
    result = Acceso("fncrudrepositoriomodulos",params).EjecutaFuncionCRUD()
    
    if result:
            return jsonify({
                'Exito': result[0]["exito"],
                'Mensaje': result[0]["mensaje"],
                'Respuesta': result[0]["respuesta"]
            })
    else:
        return jsonify({'error': 'No se obtuvo respuesta de la base de datos.'}), 500
    

"""  """



@modulosrepo_bp.route('modulocodigo',methods=['POST'])
#@jwt_required()
def CreateModuloCodigo():
    datos = request.get_json()
    #id= str(datos.get('id'))
    idrepositoriomodulo= str(datos.get('idrepositoriomodulo'))
    idusuario = str(datos.get('idusuario'))
    titulosolicitud = datos.get('titulosolicitud')
    solicitudcodigo = datos.get('solicitudcodigo')
    descripcioncodigo = datos.get('descripcioncodigo')
    codigo = datos.get('codigo')
    dia = datos.get('dia')
    operacion = 'CREATE'
    params = [operacion, None, int(idrepositoriomodulo), int(idusuario), titulosolicitud, solicitudcodigo, descripcioncodigo, codigo, dia]
    result = Acceso("fncrudmodulogeneracioncodigo",params).EjecutaFuncionCRUD()
    
    if result:
            return jsonify({
                'Exito': result[0]["exito"],
                'Mensaje': result[0]["mensaje"],
                'Respuesta': result[0]["respuesta"]
            })
    else:
        return jsonify({'error': 'No se obtuvo respuesta de la base de datos.'}), 500


@modulosrepo_bp.route('modulocodigo/consultar',methods=['POST']) 
def ReadModuloCodigoId():
    datos = request.get_json()
    idusuario = str(datos.get('idusuario'))
    idrepositoriomodulo= str(datos.get('idrepositoriomodulo'))
    dia = datos.get('dia')
    operacion = 'READIDMODULO'
    params = [operacion, None, int(idrepositoriomodulo), int(idusuario), None, None, None, None, dia]
    result = Acceso("fncrudmodulogeneracioncodigo",params).EjecutaFuncionCRUD()
    
    if result:
            return jsonify({
                'Exito': result[0]["exito"],
                'Mensaje': result[0]["mensaje"],
                'Respuesta': result[0]["respuesta"]
            })
    else:
        return jsonify({'error': 'No se obtuvo respuesta de la base de datos.'}), 500
    
