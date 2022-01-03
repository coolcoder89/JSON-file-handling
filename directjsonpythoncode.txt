import json

shopping_list = {
'Bread' : '1 pack',
'Eggs' : '1 dozen',
'Orange Juice' : '1 ltr',
'Yoghurt' : '1 kg',
'Fresh Cookies' : '1 dozen'
}

with open("shoppinglist.json",'w') as file:
  json.dump(shopping_list, file, indent = 2)

print(f"{len(shopping_list)} item(s) have been saved in the Shopping List File")

// use trinket.com python 3 mode to execute program
