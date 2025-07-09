import logging
import json


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
    # если сработает данное условие, сообщение выведется на консоле, потому что это `warning`
else:
    logging.info("The Source Language and Target Language codes are different - proceeding") # # # если сработает данное условие, сообщение не выведется на консоле потому что уровень лога info ниже чем warning