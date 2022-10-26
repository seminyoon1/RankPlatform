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
        value = response['Item']['value']
        return value

    def addItemValue():
        values = getItemValue()
        table = dynamodb.Table('Items')
        table.update_item(
        Key={
            'item_name': 'CRTgetITRANDvalue',
            'item_ID': 0
        },
        UpdateExpression='SET item_popularity = :item',
        ExpressionAttributeValues={
            ':item': values + 1
        }
        )