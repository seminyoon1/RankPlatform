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
Back End work - item, testData folders and MainWeb.py

Uses DynamoDB from AWS to store data. See DynamoDB.py for populating or updating data. 
Requires AWS CLI to run. See https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
to get started. 