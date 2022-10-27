from DBItems import addItem,createTable,getItem,addToItem,scan_Table #add DynamoDB.Items after testing

#addItem adds item to the table
#createTable creates a table. 
#getItem gets an item with specified parameter.

#createTable("Items")
#addItem('computer')
#print(getItem('computer'))
#addItem('pizza')
#print(getItem('pizza'))
#addItem("Eliot")
#addToItem('computer')
print(scan_Table())