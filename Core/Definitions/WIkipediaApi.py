import sys
import requests
from Core.Log import Log
import json
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()


class WIkipediaApi:
    log = None

    def __init__(self):
        self.log = Log()

    def get_definition(self, word):
        try:
            url = os.getenv('WIKIPEDIA_API_URL') + word

            headers = {
                'charset': 'utf-8',
                'profile': 'https://www.mediawiki.org/wiki/Specs/definition/0.8.0"',
            }

            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                self.log.logger.critical(json.dumps(response.json()))
                return None
            contents = response.json()
            if 'en' not in contents:
                return None
            contents = contents['en']

            meanings = []
            for content in contents:
                part_of_speech = content['partOfSpeech']
                if 'definitions' not in content:
                    continue

                for definition_content in content['definitions']:
                    definition = definition_content['definition']
                    if definition is None or part_of_speech is None:
                        continue
                    meanings.append({
                        'word_class': part_of_speech,
                        'definition': BeautifulSoup(definition, features="html.parser").getText().strip()
                    })

            return meanings

        except requests.exceptions.JSONDecodeError as e:
            self.log.logger.critical(str(e))
            return None
