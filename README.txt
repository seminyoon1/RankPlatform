----------RANKPLATFORM INFORMATION AND DOCUMENTATION----------
What is RankPlatform: A platform developed in order to give users randomized table elements 
to choose from. The users themselves are "ranked" by the system itself: these can include
sufficent activity, suggesting elements to include, "famous" people and more. Higher ranked
users' votes are weighted more than anonymous and low ranked votes. Currently limited to BC.

How to start: Need Flask in order to run MainWeb.py. Will generate the website using populated
testData code from data.py and data.txt. Includes usage of static and templates folders which
contain HTML and CSS code for the website.

Dev related information:
Front End work - testData, static, templates folders and MainWeb.py
Back End work - DynamoDB, testData folders and MainWeb.py

Uses DynamoDB from AWS to store data. See DynamoDB for populating or updating data. 
Requires AWS CLI to run. See https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
to get started. 

Pertinent Front End Information:

I don't know front end lol plz halp

See templates for HTML files and static for CSS files (required for Flask to access it)
See documentation for accessing python variables to html: https://flask.palletsprojects.com/en/2.2.x/quickstart/


Pertinent Back End Information:

*How to use DynamoDB folder and contents:*
The folder is split into Items - Accessing or changing Items from the AWS DynamoDB and 
Users - Same thing but for User data.
Each folder contains its own DB(folder name) file which allows you to get and store data,
a way to encrypt file name as the secondary key to prevent manual changes and a testFile
to work with the database and see immediate changes. 
The Items folder contains 'RandomItem' which enables random access to any element giving
the keys to get the item information. It also contains a template file containing bare functions.
***Important***
DynamoDB is similar to a Hash Table - Every time we read it requires capacity units, 
currently the most we can use is 25, currently set to 10. For Example: traversing the entire table 
to pick a random element would cost n capacity units and so I made another table that is easier to
access (using integer values as the key) which gives access to the actual data key.
In testFiles DO NOT abuse/change the functions - they are meant for single access.

