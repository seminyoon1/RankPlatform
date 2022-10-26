import boto3
from itemID import convertToID

#DOCUMENTATION https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
def createTable(name):
    dynamodb.create_table(
        TableName=name,
        KeySchema=[
            {
                'AttributeName': 'item_name',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'item_ID',
                'KeyType': 'RANGE',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'item_name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'item_ID',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
#print(table.creation_date_time)
def addItem(item):
    table = dynamodb.Table('Items')
    num = convertToID(item)
    if(type(item)) == str:
        table.put_item(
        Item={
                'item_name': item,
                'item_ID': num,
                'item_popularity': 0
            }
        )
    else:
        print("not a string")

#get item
def getItem(item):
    table = dynamodb.Table('Items')
    if(type(item)) == str:
        num = convertToID(item)
        response = table.get_item(
        Key={
            'item_name': item,
            'item_ID': num
            }
        )
    info = response['Item']
    return info

#update in progress NEED TO FIX
def addToItem(item)
    values = getItem(item)
    #get dict key from value to update
    if(type(item)) == str:
        num = convertToID(item)
        table.update_item(
        response = table.get_item(
        Key={
            'item_name': item,
            'item_ID': num
            },
        UpdateExpression='SET item_popularity = popularity',
        ExpressionAttributeValues={
            'popularity': value+1
        }
        )
)