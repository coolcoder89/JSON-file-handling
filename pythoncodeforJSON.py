   
import json

info_list = {
'name' : input('what is your name?'),
'Age' : input('what is your age?'),
'address' : input('what is your address?'),
'item' : input('what do you want to buy?'),
'card' : input('what is your card number?')
}

with open("infolist.json",'w') as file:
  json.dump(info_list, file, indent = 2)

print("order placed")
