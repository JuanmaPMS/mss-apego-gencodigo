import json

class Request:
    def __init__(self, pregunta):
        self.pregunta = pregunta

class RequestDecoder(json.JSONDecoder):
    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, json_dict):
        try:
            _request = Request(
                json_dict['pregunta']
                )
            return _request
        except:
            return None
