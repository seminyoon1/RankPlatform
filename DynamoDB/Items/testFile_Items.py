from DBItems import addItem,createTable,getItem,addToItem,scan_Table #add DynamoDB.Items after testing
from RandomItem.itemData import randomTable
import time
import random
#addItem adds item to the table
#createTable creates a table. 
#getItem gets an item with specified parameter.

#createTable("Items")
#addToItem('computer')
#print(scan_Table())

#change to get number of items
n = 3

seconds = time.time()
for _ in range(20):
    y = randomTable.getRandomItems(n)
bro = time.time()

print("For " + str(n) + " elements, it took on average " + str((bro-seconds)/20) + " seconds")
print(y)
