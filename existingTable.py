import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('Items')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
#print(table.creation_date_time)

table.put_item(
   Item={
        'item_name': 'Computer',
        'number': 7
    }
)

table.put_item(
   Item={
        'item_name': 'Peanuts',
        'number': 30
    }
)


#get item
response = table.get_item(
    Key={
        'item_name': 'Computer',
        'number': 7
    }
)
item = response['Item']
print(item['number'])