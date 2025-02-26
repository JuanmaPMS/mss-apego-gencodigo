import psycopg2
from Utils.Respuestas import Respuesta
from Utils.Decoders import RequestDecoder
#from db import Acceso
from flask import Blueprint, request, jsonify,Response
#from flask_jwt_extended import jwt_required
import json
from Utils.CallOpenAI import OpenAIConector
from Utils.CallOpenAIPrototipo import OpenAIProtipoConector

generaprototipo_bp = Blueprint('prototipo', __name__)

@generaprototipo_bp.route('/prototipo', methods=['POST'])
def ObtieneCodigo():
 
        #Valida el json de entrada
        params = request.get_json()
        pregunta = params.get('HU')
        EspecifTec = params.get('EspecifTec')
        
        #pregunta_ia = f"De acuerdo a la siguiente historia de usuario  '{pregunta.capitalize()}'" + ObtieneDinEstatico(EspecifTec) 
        pregunta_ia = f"Genera un formulario con base a la siguiente descripción: '{pregunta.capitalize()}'. Tambien incluye las siguientes especificaciones: {EspecifTec}.";
        IniciaOAI = OpenAIProtipoConector()
        RespuestaOAI = IniciaOAI.enviarOPENAI(pregunta_ia).replace('```html', '').replace('```', '')
        #return Response(RespuestaOAI, mimetype='text/html')
    
        if RespuestaOAI != '':
            Response = {'Exito': True, 'Resultado': RespuestaOAI, 'Detalle': ''}
        else:
            Response = {'Exito': False, 'Resultado': 'No se obtuvieron resultados.', 'Detalle': ''}
        return Response
        
        
def ObtieneDinEstatico(EspecifTec:str)->str:
    cadena = """ 

                genera el código HTML que cumpla con esos criterios cuidando la estetica y correcta proporcion entre los elemntos del formulario, 
                además incluye el siguiente CDN en la etiqueta <head>   <link href="https://framework-gb.cdn.gob.mx/assets/styles/main.css" rel="stylesheet"> y el siguiente cdn:  
                <script src="https://framework-gb.cdn.gob.mx/gobmx.js"></script><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script> antes de finalizar la etiqueta </body> inicializa de esta forma <script>
                $gmx(document).ready(function() {
                    ...
                });</script> 
                """
    cadena2 = ""
    if len(EspecifTec.replace(" ", "")) > 0:
        cadena2 = "Contempla lo siguiente: " + EspecifTec + " Tambien es sumamente importante que "           
    cadena3 = """
                si se usan tabs de boostrap no agregues la clase show, tambien siempre antes de esta etiqueta </body> agrega las etiquetas <br><br>

                despues de <div class='container' style=''> o del div principal agrega <br><br>


                adicional por favor agrega estos elementos HTML 
                    <div id="loader">
                        <div class="spinner"></div>
                        <p>Cargando...</p>
                    </div>
                Estos elementos de CSS:
                    <style>
                        #loader {
                            position: fixed;
                            width: 100%;
                            height: 100%;
                            background: rgba(255, 255, 255, 0.9);
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            flex-direction: column;
                            font-size: 1.5rem;
                            font-weight: bold;
                            color: #333;
                            z-index: 9999;
                        }
                        .spinner {
                            border: 6px solid #f3f3f3;
                            border-top: 6px solid #3498db;
                            border-radius: 50%;
                            width: 50px;
                            height: 50px;
                            animation: spin 1s linear infinite;
                        }
                        @keyframes spin {
                            0% { transform: rotate(0deg); }
                            100% { transform: rotate(360deg); }
                        }

                    </style>
                y por ultimo este script despues del codigo "$gmx(document).ready(function()":

                $(document).ready(function() {
                    
                        //Para visualizacion de tabs
                        var tabs = document.querySelectorAll(".tab-pane");
                        document.querySelectorAll(".tab-pane").forEach(el => {    
                            el.classList.remove("show")
                        });
     
                            let interval = setInterval(function() {
                                console.log("Ejecutando...");
                                if (document.querySelector("footer.main-footer")) {
                                    $("#loader").fadeOut();
                                    $(".container").fadeIn();
                                    clearInterval(interval);
                                }
                            }, 200);
                        });
                Por favor NO INCLUYAS introducción ni conclusión, UNICAMENTE el código HTML solicitado.
                """
                
                
    #cadenafinal = "genera el código HTML que cumpla con esos criterios cuidando la estetica y correcta proporcion entre los elementos del formulario. Por favor NO INCLUYAS introducción ni conclusión, UNICAMENTE el código HTML solicitado." + " Contempla lo siguiente: " + EspecifTec #+ ". Por favor NO INCLUYAS introducción ni conclusión, UNICAMENTE el código HTML solicitado."
    
    
    cadenafinal = "genera un formulario con tres secciones, la primera seccion es de datos personales segunda sección es de patologías pre existentes y la tercera debe tener sección de patologías familiares"
    
    #return cadena + cadena2 + cadena3
    return cadenafinal
   