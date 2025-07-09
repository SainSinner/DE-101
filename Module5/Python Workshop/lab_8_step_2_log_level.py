
import logging
import json

# уровень DEBUG означает, что все уровни логирования будут сохранены в файл
logging.basicConfig(filename='example.log',level=logging.DEBUG)

json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr"
        }
    ]
}
"""

json_input = json.loads(json_string)


SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']


if SourceLanguageCode == TargetLanguageCode:
    logging.warning("The SourceLanguageCode is the same as the TargetLanguageCode - stopping")
else:
    logging.info("The Source Language and Target Language codes are different - proceeding")