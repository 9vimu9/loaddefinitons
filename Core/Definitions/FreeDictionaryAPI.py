import requests

URL = 'https://api.dictionaryapi.dev/api/v2/entries/en/'


class FreeDictionaryAPI:

    def get_definition(self, word):
        response = requests.get(URL + word)
        if response.status_code != 200:
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
