test_realm = ('Shadow_Moses', 'Outer_Heaven', 'Big_Shell')
print('tuple:', test_realm)

first_realm = test_realm[0]
print(first_realm, '1')

second_realm = test_realm[1]
print(second_realm, '2')

third_realm = test_realm[0]
print(third_realm, '3')

print(len(test_realm))

#print(test_realm['cant_add'])   #immutable
#test_realm.append('cant_add')   #immutable

####################

MSG = {'USP': 2, 'Health_Kit': 4, 'Cigarette': 7}
print(MSG)

print('containing following values', MSG.values())
print('items in inventory', MSG.keys())

#print(len(MSG))

MSG['Stealth_Kit'] = 2  #adding 2 Stealth_Kits
print(MSG)

MSG.pop('USP')   #need to use .pop / .remove will not work on dictionaries
print(MSG)

#MSG.clear()
#print(MSG)

#MSG.append('Test')   #no .append just add as seen above




