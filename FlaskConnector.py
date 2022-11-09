from DynamoDB.Items.DBItems import getItem, resetItem, addToItem
from DynamoDB.Items.RandomItem.itemData import randomTable

def getDictItems(name):
    dictItems = {}
    setNames = randomTable.getRandomItems(name)
    if type(setNames) != str:
        for i in setNames:
            dictItems[i] = int(getItem(i)['item_popularity'])
        return dictItems
    else:
        return setNames

def adminResetItem(name):
    resetItem(name)
    
def increasePopularity(name):
    addToItem(name)