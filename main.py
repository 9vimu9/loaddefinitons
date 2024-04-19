import sys

from Core.MySqlConnector import MySQLConnector
from Core.Lists.JeremyRifkinWordlist import file_to_list
from Core.Models.Corpus import Corpus
from Core.Definitions.FreeDictionaryAPI import FreeDictionaryAPI
from Core.Models.Definition import Definition

if __name__ == '__main__':
    limits = sys.argv
    start_index = int(sys.argv[1])
    end_index = int(sys.argv[2])
    word_list = file_to_list()
    word_list = word_list[start_index:end_index]

    definition_api = FreeDictionaryAPI()
    corpus = Corpus()
    definition = Definition()
    for word in word_list:
        if len(corpus.find_by_word(word)) > 0:
            continue
        definitions = definition_api.get_definition(word)
        if definitions is None:
            continue
        corpus_dict = corpus.save(word)
        if corpus_dict is None:
            continue

        for meaning in definitions:
            definition.save(corpus_dict['id'], meaning['word_class'], meaning['definition'])
