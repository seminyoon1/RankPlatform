from DynamoDB.Items.DBItems import getItem
from DynamoDB.Items.RandomItem.itemData import randomTable

def getDictItems(n):
    dictItems = {}
    setNames = randomTable.getRandomItems(n)
    if type(setNames) != str:
        for i in setNames:
            dictItems[i] = int(getItem(i)['item_popularity'])
        return dictItems
    else:
        return setNames