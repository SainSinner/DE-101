import boto3

client = boto3.client('translate', region_name='eu-north-1')

def translate_text():  # Объявляем функцию
    response = client.translate_text(
        Text='Всем пирвет, я новенький в AWS',  # Присваиваем строчное значение к переменной Text
        SourceLanguageCode='ru',  # Согласно документации, мы используем обозначение языка из двух букв (en = English)
        TargetLanguageCode='en'  # Аналогично (fr = French)
    )
    print(response)

def main():
    translate_text()

if __name__=="__main__":
    main()
