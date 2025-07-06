import boto3


def translate_text(text, source_language_code, target_language_code):
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text,
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code
    )
    print(response)

def main():
    translate_text(text='Всем hello, я новенький в AWS!'
                   , source_language_code='ru'
                   , target_language_code='en')

if __name__=="__main__":
    main()
