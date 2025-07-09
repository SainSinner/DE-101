# встроенные библиотеки
import argparse
import json

# установленные библиотеки
import boto3

# аргументы
parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True)

args = parser.parse_args()

# функции
def open_input():
    with open(args.filename) as file_object:
        contents = json.load(file_object)
        return contents['Input'][0]

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

# Функция Main - в которой мы вызываем другие функции
def main():
    kwargs = open_input()
    translate_text(**kwargs)

if __name__ == "__main__":
    main()