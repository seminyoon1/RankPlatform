import boto3
import random
#it works :D
class randomTable:
    #get total num of items in the table
    def getItemValue():
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Items')
        response = table.get_item(
        Key={
            'item_name': 'CRTgetITRANDvalue',
            'item_ID': 0
            }
        )
        value = response['Item']['item_popularity']
        return value

    def addItemValue():
        dynamodb = boto3.resource('dynamodb')
        value = randomTable.getItemValue()
        table = dynamodb.Table('Items')
        table.update_item(
        Key={
            'item_name': 'CRTgetITRANDvalue',
            'item_ID': 0
        },
        UpdateExpression='SET item_popularity = :item',
        ExpressionAttributeValues={
            ':item': value + 1
        }
        )
    #def getRandomItem():
