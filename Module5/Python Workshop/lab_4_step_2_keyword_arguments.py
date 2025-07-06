import boto3


def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)


def main():
    translate_text(Text='Всем hello, я новенький в AWS!'
                   , SourceLanguageCode='ru'
                   , TargetLanguageCode='en')


if __name__ == "__main__":
    main()
