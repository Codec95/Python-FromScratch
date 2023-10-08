test_num = 256
print(test_num)

test_num /= 2
print(int(test_num))

test_conv = 42.256
print('original value', test_conv)
print('converted to int', int(test_conv))
print('converted to complex', complex(test_conv)) #Integer converted
#print('converted to complex', (test_conv)) #Complex converted
print('converted to complex', float(round(test_conv, 2))) #Float converted // rounded 2 digits after

############################

test_dword = 0
print(bool(test_dword)) #Bool always True if not set to False(0)
print(test_dword == test_num)

print(test_dword or test_num > 1)

life = 42
health = 2

print(bool(life or health <= 0)) #something's not right!!

############################

items = ['Helmet', 'Armor', 'Sword']
print(items)

items.append('Coin')
print(items)    #added Coin to items
items.pop()
print(items)    #deleted last item in items
items.insert(2, 'Disc')
print(items)    #inserted Disc into items (3)
#items.clear()
#print(items)   #items list cleared
items.remove('Helmet')
print(items)    #Helmet removed from items

print(len(items))
print(max(items))
print(min(items))

############################

level_hub = [['Cow', 'Wasteland', 'City'],                     #0
            ['Lava', 'Sky', 'Castle'],                         #1
            ['Underground', 'New Haven', 'Black Mesa']]        #2

print(level_hub[1])

level_hub[1].append('Test')
print(level_hub)
level_hub[2].insert(2, 'Nakatomi Plaza')   #long live John!
print(level_hub)

