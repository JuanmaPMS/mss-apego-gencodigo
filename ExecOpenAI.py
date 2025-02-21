from openai import OpenAI
from decouple import config

class Exec:
    def enviarOPENAI(self, tablas: str, pregunta: str) -> str:
        
        client = OpenAI(api_key=config('API_KEY_OPENAI'))
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente experto en analizar tablas y crear scripts SQL."},
            {"role": "user", "content": f"Aquí tienes un set de tablas para analizar: {tablas}"},
            {"role": "user", "content": f"Las preguntas SOLO deben ser orientadas a la generación de Scripts"},
            {"role": "user", "content": f"Si no tienes los suficientes datos para realizar la operacion indicada, por favor solicita más información."},
            {"role": "user", "content": f"Solo genera Queries, SELECT no puedes crear vistas, si la pregunta pide una vista devuelve un querie"},
            {"role": "user", "content": f"No puedes generar ningun objeto de base de datos, unicamente instrucciones SELECT"},
            {"role": "user", "content": f"Si se solicita un querie diferente a una Instruccion Select, indica que solo puedes generar instrucciones SELECT y que recomiendas usar la opcion  'Materializar Vista'"},
            {"role": "user", "content": f"Por favor no agregues introduccion, explicacion o comentarios adicionales."},
            {"role": "user", "content": f"Pregunta: {pregunta}"}
                ])
        obj =  response.choices[0].message.content
        return obj
    

    def enviarOPENAIRefinaQuery(self, pregunta: str) -> str:
        ejemplo = [
            {"role": "system", "content": "Eres un asistente experto en analizar tablas y crear scripts SQL."},
            {"role": "user", "content": "Condensa la siguiente consulta de tal forma que ocupe menos caracteres y sea mas legible, las llaves foraneas existentes incluyelas en la instruccion create table "},
            {"role": "user", "content": f"Por favor no agregues introduccion, explicacion o comentarios adicionales."},
            {"role": "user", "content": f"Pregunta: {pregunta}"}
                ]
        client = OpenAI(api_key=config('API_KEY_OPENAI'))
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente experto en analizar tablas y crear scripts SQL."},
            {"role": "user", "content": "Condensa la siguiente consulta de tal forma que ocupe menos caracteres y sea mas legible, las llaves foraneas existentes incluyelas en la instruccion create table "},
            {"role": "user", "content": f"Por favor no agregues introduccion, explicacion o comentarios adicionales."},
            {"role": "user", "content": f"Pregunta: {pregunta}"}
                ])
        print("Pregunta", ejemplo);
        obj =  response.choices[0].message.content
        return obj  
    
    def enviarFnOPENAI(self, tablas: str, pregunta: str) -> str:
        
        client = OpenAI(api_key=config('API_KEY_OPENAI'))
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente experto en creación de funciones SQL."},
            {"role": "user", "content": f"Aquí tienes un set de tablas para analizar: {tablas}"},
            {"role": "user", "content": f"Las preguntas SOLO deben ser orientadas a la generación de Scripts de funciones"},
            {"role": "user", "content": f"Si no tienes los suficientes datos para realizar la operacion indicada, por favor solicita más información."},
            {"role": "user", "content": f"Solo genera código de funciones"},
            {"role": "user", "content": f"Siempre incluye CREATE OR REPLACE FUNCTION"},
            #{"role": "user", "content": f"En el retorno de la función, a todas las columnas agrega 'r_' al inicio del nombre"},
            #{"role": "user", "content": f"En el retorno de la función, considera las conversiones necesarias respecto al tipo de dato"},
            #{"role": "user", "content": f"En el retorno de la función, el tipo de dato serial reemplazalo por integer"},
            {"role": "user", "content": f"Si se solicita un querie diferente a una Creación de Función, indica que solo puedes generar scripts para creación de funciones"},
            {"role": "user", "content": f"Por favor no agregues introduccion, explicacion o comentarios adicionales."},
            {"role": "user", "content": f"Pregunta: {pregunta}"}
                ])
        obj =  response.choices[0].message.content
        return obj
    
    def enviarOPENAIRefinaFn(self, pregunta: str) -> str:
        
        client = OpenAI(api_key=config('API_KEY_OPENAI'))
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente experto en creación de funciones SQL."},
            {"role": "user", "content": "Por favor analiza el script y corrige errores de lógica"},
            {"role": "user", "content": "Por favor verifica que las columnas que se retornan no se llamen igual que las columnas de las tablas involucradas"},
            {"role": "user", "content": "Por favor agrega conversiones de tipos explícitas en todos los retornos de la función."},
            {"role": "user", "content": f"Por favor no agregues introduccion, explicacion o comentarios adicionales."},
            {"role": "user", "content": f"Pregunta: {pregunta}"}
                ])
        obj =  response.choices[0].message.content
        return obj
   