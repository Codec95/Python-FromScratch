# Collections

# Dictionaries

items = {'Knife':4, 'Health Kit': 3, 'Potion': 2}
print(items['Knife'])

items['Knife'] = 2
print(items)
items['Coin'] = 42
print(items)

items = {'Knife':4, 'Health Kit': 3, 'Potion': 2}
# print(items['Coin'])    #Crash
print(items.get('Coin'))
print(items.keys())
print(items.values())

items.pop('Knife')
print(items)

