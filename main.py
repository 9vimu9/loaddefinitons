from Core.MySqlConnector import MySQLConnector
from Core.Lists.JeremyRifkinWordlist import file_to_list
from Core.Corpus import Corpus
from Core.Definitions.FreeDictionaryAPI import FreeDictionaryAPI
from Core.Definition import Definition

if __name__ == '__main__':
    word_list = file_to_list()
    word_list = word_list[:10]

    definition_api = FreeDictionaryAPI()
    corpus = Corpus()
    definition = Definition()
    for word in word_list:
        definitions = definition_api.get_definition(word)
        if definitions is None:
            continue
        corpus_dict = corpus.save(word)
        if corpus_dict is None:
            continue

        for meaning in definitions:
            definition.save(corpus_dict['id'], meaning['word_class'], meaning['definition'])
