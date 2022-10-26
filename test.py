import boto3

table = boto3.resource('dynamodb').Table('Items')

table.put_item(
   Item = {
        'item_name': 'computer',
        'item_ID': 0,
        'item_popularity': 0
    }
)
# get item
response = table.get_item(
    Key={
        'item_name': 'computer',
        'item_ID': 0
    }
)
item = response['Item']
print(item)
