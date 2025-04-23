import requests
from decouple import config

class OpenAIProtipoConector:


    def __init__(self):
        self.api_key_ = config('API_KEY_OPENAI')
        self.endpoint_ = config('ENDPOINT_OPENAI')
       # self.model_ = config('MODELO_OPENAI_FINE_TUNNING')
        self.model_ = config('MODELO_OPENAI')

    def enviarOPENAI(self, pregunta: str) -> str:
        api_key = self.api_key_
        endpoint = self.endpoint_
        headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }
        data = {
                'model': self.model_,
                "messages": [
                {
                "role": "user",
                "content": pregunta
                }
            ]
            }
        response = requests.post(endpoint, headers=headers, json=data)
        resultado = response.json()
        
        return resultado['choices'][0]['message']['content']
    
