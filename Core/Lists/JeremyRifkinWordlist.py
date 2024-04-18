import csv


def file_to_list():
    word_list = []
    with open('Sources/jeremy-rifkin-wordlist.txt', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            word_list.append(row[0])

    return word_list
