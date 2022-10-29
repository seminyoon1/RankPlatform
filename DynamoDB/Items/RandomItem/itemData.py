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
            'item_name': 'CRTgetITRANDvalue'
            }
        )
        value = response['Item']['item_popularity']
        return int(value)

    def addItemValue():
        dynamodb = boto3.resource('dynamodb')
        value = randomTable.getItemValue()
        table = dynamodb.Table('Items')
        table.update_item(
        Key={
            'item_name': 'CRTgetITRANDvalue'
        },
        UpdateExpression='SET item_popularity = :item',
        ExpressionAttributeValues={
            ':item': value + 1
        }
        )
    
    def getRandomItems(num):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Random_Items')

        totalVal = randomTable.getItemValue() - 1
        numArr = random.sample(range(0, totalVal), num)
        returnArr = []

        if totalVal >= num:
            for i in numArr:
                response = table.get_item(
                Key={
                'valueItem': i
                }
                )
                returnArr.append(response['Item']['item_name'])
        else:
            return "Unable to get all elements!"

        return returnArr
