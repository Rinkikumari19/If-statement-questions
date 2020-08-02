
import json
with open('user.json','r') as data_file:    
    data = json.load(data_file)

users = data['users']

for user in users:
  counter = 0
  print ("users full name is ") + users['firstName'] + ' ' + users['lastName']
  while counter < len(user['details']):
    print ("users mobile number is ") + user['details'][counter]['mobileNo']
    print ("users age  is ") + user['details'][counter]['age']
    print ("users city is ") + user['details'][counter]['city']

my_file = open("user.json",'r')
data = my_file.read()
print(data)