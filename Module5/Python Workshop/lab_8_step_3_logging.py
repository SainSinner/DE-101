
# встроенные пакеты
import argparse
import json
import logging
import boto3

# уровень DEBUG означает, что все уровни логирования будут сохранены в файл
logging.basicConfig(filename='translate.log',level=logging.DEBUG)

# добавление аргументов
parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True)

args = parser.parse_args()

# функции

# загружаем json строку
def open_input():
    with open(args.filename) as file_object:
        contents = json.load(file_object)
        return contents['Input']

# функция Boto3, которая использует Amazon Translate для перевода текста и возвращает только переведенный текст
def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText'])

# цикл для перебора элементов JSON файла
def translate_loop():
    input_text = open_input()
    for item in input_text:
        if input_validation(item) == True:
            translate_text(**item)
        else:
            raise SystemError

# функция для проверки данных из JSON строки
def input_validation(item):
    languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF",
                "nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it",
                "ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es",
                "sw","sv","tl","ta","th","tr","uk","ur","vi"
                ]
    json_input=item
    SourceLanguageCode = json_input['SourceLanguageCode']
    TargetLanguageCode = json_input['TargetLanguageCode']

    if SourceLanguageCode == TargetLanguageCode:
        logging.warning("The SourceLanguageCode is the same as the TargetLanguageCode - nothing to do")
        logging.debug(f"SourceLanguageCode:{SourceLanguageCode}\nTargetLanguageCode:{TargetLanguageCode}")
        return False
    elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
        logging.warning("Neither the SourceLanguageCode and TargetLanguageCode are valid - stopping")
        logging.debug(f"SourceLanguageCode:{SourceLanguageCode}\nTargetLanguageCode:{TargetLanguageCode}")
        return False
    elif SourceLanguageCode not in languages:
        logging.warning("The SourceLanguageCode is not valid - stopping")
        logging.debug(f"SourceLanguageCode:{SourceLanguageCode}")
        return False
    elif TargetLanguageCode not in languages:
        logging.warning("The TargetLanguageCode is not valid - stopping")
        logging.debug(f"TargetLanguageCode:{TargetLanguageCode}")
        return False
    elif SourceLanguageCode in languages and TargetLanguageCode in languages:
        logging.info("The SourceLanguageCode and TargetLanguageCode are valid - proceeding")
        return True
    else:
        logging.warning("There is an issue")
        logging.debug(f"SourceLanguageCode:{SourceLanguageCode}\nTargetLanguageCode:{TargetLanguageCode}")
        return False

# функция Main для вызова других функций
def main():
    translate_loop()

if __name__ == "__main__":
    main()
