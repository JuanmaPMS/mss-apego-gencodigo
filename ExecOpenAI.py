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
            {"role": "user", "content": f"Las preguntas SOLO deben ser orientadas a la generación de Scripts y objetos SQL."},
            {"role": "user", "content": f"Si no tienes los suficientes datos para realizar la operacion indicada, por favor solicita más información."},
            {"role": "user", "content": f"Por favor no agregues introduccion, explicacion o comentarios adicionales."},
            {"role": "user", "content": f"Pregunta: {pregunta}"}
                ])
        obj =  response.choices[0].message.content
        return obj
    

    def enviarOPENAIRefinaQuery(self, pregunta: str) -> str:
        
        client = OpenAI(api_key=config('API_KEY_OPENAI'))
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente experto en analizar tablas y crear scripts SQL."},
            {"role": "system", "content": "Condensa la siguiente consulta de tal forma que ocupe menos caracteres y sea mas legible, las llaves foraneas existentes incluyelas en la instruccion create table "},
            {"role": "user", "content": f"Por favor no agregues introduccion, explicacion o comentarios adicionales."},
            {"role": "user", "content": f"Pregunta: {pregunta}"}
                ])
        obj =  response.choices[0].message.content
        return obj  
   