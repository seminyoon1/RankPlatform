import boto3
import random

class randomTable:
    #get total num of items in the table
    def getItemValue():
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Items')
        response = table.get_item(
        Key={
            'item_name': 'CRTgetITRANDvalue'
            }
        )
        value = response['Item']['item_popularity']
        return int(value)

    def addItemValue(num):
        if type(num) == int:
            dynamodb = boto3.resource('dynamodb')
            value = randomTable.getItemValue()
            table = dynamodb.Table('Items')
            table.update_item(
            Key={
                'item_name': 'CRTgetITRANDvalue'
            },
            UpdateExpression='SET item_popularity = :item',
            ExpressionAttributeValues={
                ':item': value + num
            }
            )

    def getRandomItems(num):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Random_Items')

        totalVal = randomTable.getItemValue()
        returnSet = set()

        if totalVal >= num:
            numArr = random.sample(range(totalVal), num)
            for i in range(len(numArr)):
                response = table.get_item(
                Key={
                'valueItem': numArr[i]
                }
                )
                returnSet.add(response['Item']['item_name'])
            return returnSet
        else:
            return "Unable to get all elements!"
