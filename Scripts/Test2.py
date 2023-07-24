
#variable
num = 267.02

print(num)

if num%2 == 0:
	print("it's even!")

else:
	print("it's not even!")

print('num is', type(num))

if type(num) is float:
	print('output is float')

elif type(num) is int:
	print('output is int')

else:
	print('output is complex')

#converter
print('converted to int', int(num))
print('converted to float', float(num))
print('converted to complex', complex(num))



#Listen
#fistList
var = ('dword', 'string', 'batch')
#secondList
lis = ('Test', 42)

#fist
print('first list', var,'is', len(var), 'items long')
#second
print('second list', lis,'is', len(lis), 'items long')
#combined
print('both lists combined', var+lis,'is', len(var) + len(lis), 'items long')


x = ['Test']
x.append(24)
print(x)

#Dictionary
dic = {'First output': (0o2, 0o4, 0o6)}
dic2 = {'Second output': (0o2, 0o4, 0o6)}
print(dic)
print(dic['First output'][1])


dic.update(dic2)
dic['Third output'] = (2, 4, 6)
print('updated dictionary:', dic)

print(dic['Third output'])

