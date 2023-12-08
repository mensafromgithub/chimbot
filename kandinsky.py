import json
from time import sleep
from requests import get, post
from base64 import b64decode

from os import getenv
from dotenv import load_dotenv
from pathlib import Path


dotenv_path = Path('config.env')
load_dotenv(dotenv_path=dotenv_path)


class Text2ImageAPI:
    def __init__(self, url, api_key, secret_key):
              self.URL = url
              self.AUTH_HEADERS = {
                  'X-Key': f'Key {api_key}',
                  'X-Secret': f'Secret {secret_key}',
                   }

    def get_model(self):
              response = get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
              data = response.json()
              return data[0]['id']

    def generate(self, prompt, model, style='DEFAULT', aprompt='', images=1, width=1024, height=1024):
              params = {
                "type": "GENERATE",
                "style": style,
                "numImages": images,
                "width": width,
                "height": height,
                "negativePromptUnclip": aprompt,
                "generateParams": {
                    "query": f"{prompt}"
                       }
                    }

              data = {
                  'model_id': (None, model),
                  'params': (None, json.dumps(params), 'application/json')
              }
              response = post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
              data = response.json()
              return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
              while attempts > 0:
                  response = get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
                  data = response.json()
                  if data['status'] == 'DONE':
                      return [b64decode(i) for i in data['images']]

                  attempts -= 1
                  sleep(delay)
              return 'OUT OF TIME'


api = Text2ImageAPI('https://api-key.fusionbrain.ai/', getenv('KANDINSKY_API_KEY'), getenv('KANDINSKY_SECRET_KEY'))
model_id = api.get_model()
