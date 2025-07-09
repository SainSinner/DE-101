import argparse  # argparse является встроенным пакетом, и его нужно импортировать
import boto3

# присваиваем переменной парсера значение argparse.ArgumentParser()
# те. этой командой мы создали парсер
parser = argparse.ArgumentParser(
    description="Provides translation between one source language and another of the same set of languages.")

# добавьте каждый аргумент используя метод parser.add_argument()
# первый аргумент, который мы добавляем отвечает за значение текста, который мы хотим перевести
parser.add_argument(
    '--text',
    # dest="Text",
    type=str,
    help="The text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character set, this may be fewer than 5,000 characters",
    required=True
)

parser.add_argument(
    '--source-language-code',
    # dest="SourceLanguageCode",
    type=str,
    help="The language code for the language of the source text. The language must be a language supported by Amazon Translate.",
    required=True
)

parser.add_argument(
    '--target-language-code',
    # dest="TargetLanguageCode",
    type=str,
    help="The language code requested for the language of the target text. The language must be a language support by Amazon Translate.",
    required=True
)

parser.add_argument(
    '--terminology-names',
    # dest="TerminologyNames",
    type=tuple,
    help="The name of a terminology list file to add to the translation job. This file provides source terms and the desired translation for each term. A terminology list can contain a maximum of 256 terms. You can use one custom terminology resource in your translation request.",
    required=False,
    default=()
)

# код ниже:
# - проанализирует командную строку
# - разделит ввод на аргументы
# - конвертирует каждый аргумент в тот тип данных, который мы указали выше

args = parser.parse_args()

print(args)

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)


def main():
    # vars() - это встроенная функция, которая возвращает данные в виде словаря
    translate_text(**vars(args))


if __name__ == "__main__":
    main()
