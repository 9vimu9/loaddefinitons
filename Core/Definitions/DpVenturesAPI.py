import requests
from Core.Log import Log
import json
import os
from dotenv import load_dotenv

load_dotenv()


class DpVenturesAPI:
    log = None

    def __init__(self):
        self.log = Log()

    def get_definition(self, word):
        try:
            url = os.getenv('DP_VENTURES_API_URL') + word + "/definitions"

            headers = {
                "X-RapidAPI-Key": os.getenv('DP_VENTURES_API_KEY'),
                "X-RapidAPI-Host": os.getenv('DP_VENTURES_HOST')
            }

            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                self.log.logger.critical(json.dumps(response.json()))
                return None
            contents = response.json()
            definitions = contents['definitions']
            if definitions is None:
                return None
            meanings = []
            for content in definitions:
                part_of_speech = content['partOfSpeech']
                definition = content['definition']
                if definition is None or part_of_speech is None:
                    continue
                meanings.append({
                    'word_class': part_of_speech,
                    'definition': definition
                })
            return meanings

        except requests.exceptions.JSONDecodeError as e:
            self.log.logger.critical(str(e))
            return None
