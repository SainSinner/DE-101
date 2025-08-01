import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('Movies')

print("Movies from 2001")

response = table.query(
    KeyConditionExpression=Key('year').eq(2001)
)

for i in response['Items']:
    print(i['year'], ":", i['title'])