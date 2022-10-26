import boto3
from DynamoDB.itemID import convertToID #add DynamoDB.itemID after testing

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
def addItem(item):
    table = dynamodb.Table('Items')
    if(type(item)) == str:
        num = convertToID(item)
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
    else:
        print("not a string")
    info = response['Item']
    return info

#updated - add 1 popularity to item: popularity sujected to change based on user info
def addToItem(item):
    dictValues = getItem(item) #fix values to get element (values return a dict)
    values = dictValues["item_popularity"]
    table = dynamodb.Table('Items')
    #get dict key from value to update
    if(type(item)) == str:
        num = convertToID(item)
        table.update_item(
        Key={
            'item_name': item,
            'item_ID': num
        },
        UpdateExpression='SET item_popularity = :item',
        ExpressionAttributeValues={
            ':item': values + 1
        }
        )