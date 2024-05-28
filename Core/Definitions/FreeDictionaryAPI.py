import requests
from Core.Log import Log
import json
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('FREE_DICTIONARY_API_URL')


class FreeDictionaryAPI:
    log = None

    def __init__(self):
        self.log = Log()

    def get_definition(self, word):
        try:
            response = requests.get(URL + word)
            if response.status_code != 200:
                self.log.logger.critical(json.dumps(response.json()))
                return None
            contents = response.json()
            meanings = []
            for content in contents:
                for meaning in content['meanings']:
                    word_class = meaning['partOfSpeech']
                    for definition in meaning['definitions']:
                        meanings.append({
                            'word_class': word_class,
                            'definition': definition['definition']
                        })
            return meanings
        except requests.exceptions.JSONDecodeError as e:
            self.log.logger.critical(str(e))
            return None
