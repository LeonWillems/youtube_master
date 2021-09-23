import diagnostics
import csv
from inspect import getmembers, isfunction

def read_file():
    directory = '../data/'
    file_name = input('What is the name of your file? ')
    print('')
    entries = []

    with open(directory + file_name, 'r', encoding='utf8') as csvfile:
        video_reader = csv.reader(csvfile)
        for row in video_reader:
            entries.append(row)

    return entries


def analyzer(entries):
    print('Hello, welcome to the Youtube Trending Analyzer')

    functions = getmembers(diagnostics, isfunction)
    print('Currently, we have the following functions:')
    for idx, func in enumerate(functions):
        print(f'[{idx}] {func[0]}')

    number = input('What would you like to know? ')
    print()

    obtained_function = getattr(diagnostics, functions[int(number)][0])
    obtained_function(entries)

    return
