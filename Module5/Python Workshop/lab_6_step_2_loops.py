# встроенные пакеты
import argparse
import json

from fastavro.schema import load_schema
from fastavro import validate

# установленный пакет
import boto3

# добавление аргументов
parser = argparse.ArgumentParser(
    description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True)
parser.add_argument(
    '--path-to-file-avro-schema',
    dest='path_to_file_avro_schema',
    type=str,
    help="The path to the file with validation schema. The file should be valid avcs and type of file should be .avsc.",
    required=True)

args = parser.parse_args()


# вспомогательные функции
def open_input():
    """This function returns a dictionary containing the contents of the Input section in the input file"""
    with open(args.filename) as file_object:
        contents = json.load(file_object)
        # Добавим валидацию Json файла avro schema
        avro_schema = load_schema(schema_path=args.path_to_file_avro_schema)
        validate(datum=contents, schema=avro_schema)
    return contents['Input']


# функция Boto3, которая использует Amazon Translate для перевода текста и возвращает только переведенный текст
def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText'])


# цикл для перебора элементов JSON файла
def translate_loop():
    input_text = open_input()
    for item in input_text:  # тут мы перебираем словари из файла
        if input_validation(item) == True:
            translate_text(**item)
        else:
            raise SystemError


# функция для проверки данных из JSON строки
def input_validation(item):
    languages = ["af", "sq", "am", "ar", "az", "bn", "bs", "bg", "zh", "zh-TW", "hr", "cs", "da", "fa-AF",
                 "nl", "en", "et", "fi", "fr", "fr-CA", "ka", "de", "el", "ha", "he", "hi", "hu", "id", "it",
                 "ja", "ko", "lv", "ms", "no", "fa", "ps", "pl", "pt", "ro", "ru", "sr", "sk", "sl", "so", "es",
                 "sw", "sv", "tl", "ta", "th", "tr", "uk", "ur", "vi"
                 ]
    json_input = item
    SourceLanguageCode = json_input['SourceLanguageCode']
    TargetLanguageCode = json_input['TargetLanguageCode']

    if SourceLanguageCode == TargetLanguageCode:
        print("The SourceLanguageCode is the same as the TargetLanguageCode - nothing to do")
        return False
    elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
        print("Neither the SourceLanguageCode and TargetLanguageCode are valid - stopping")
        return False
    elif SourceLanguageCode not in languages:
        print("The SourceLanguageCode is not valid - stopping")
        return False
    elif TargetLanguageCode not in languages:
        print("The TargetLanguageCode is not valid - stopping")
        return False
    elif SourceLanguageCode in languages and TargetLanguageCode in languages:
        print("The SourceLanguageCode and TargetLanguageCode are valid - proceeding")
        return True
    else:
        print("There is an issue")
        return False


# функция Main - для вызова других функций
def main():
    translate_loop()


if __name__ == "__main__":
    main()
