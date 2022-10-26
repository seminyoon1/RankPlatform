import boto3
#TRYING TO GET THIS TO WORK :(
class randomTable:
    #get total num of items in the table
    def getItemValue():
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Random_Items')
        response = table.get_item(
        Key={
            'item_name': 'CRTgetITRANDvalue',
            'item_ID': 0
            }
        )
        value = response['Item']['valueItem']
        return value

    def addItemValue():
        dynamodb = boto3.resource('dynamodb')
        value = randomTable.getItemValue()
        table = dynamodb.Table('Random_Items')
        table.update_item(
        Key={
            'item_name': 'CRTgetITRANDvalue',
            'item_ID': 0
        },
        UpdateExpression='SET valueItem = :item',
        ExpressionAttributeValues={
            ':item': value + 1
        }
        )
        print("Does this work?")