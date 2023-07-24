

# math

x = 64

print('compiling', x + 24)
print('compiling', x // 5, '//',  'rest', x % 5)

# list // tuple // dict

y = (24, 48, 96)
z = ('test')

print(y[2])

u = [0o2, 0o4, 0o6]
i = ['test']

print(u)
print(u + i)
u.append(24)
print(u[3])


dict = {"test_1":(24, 48, 96), "test_2":(24.2, 48.2, 96.2)}
print(dict)
print(dict["test_1"])


# scripts

num2 = 88

if num2 == 24:
	print('is 24!')

elif num2 <= 48:
	print('to small')

else:
	print('to big')


ran = [2, 4, 5, 6, 8]

for v in ran:
	if v % 2 == 0:
		print(v, 'even')

	else:
		print(v, 'odd')

for v2 in range(0, 22, 2):
	print(v2 ** 2)

n = 12

while n <= 22:
	print(n // 4)
	n = n + 1


# functions

def test_funtion(var):
	return(int(var))


print(test_funtion(55.2))


	# converter

def converter_int(var2):
	return(int(var2))
 
def converter_float(var2):
	return(float(var2))

def converter_complex(var2):
	return(complex(round(var2, 2)))

def converter_all(var2):
	print("###NUMBER_CONVERTER_BY_ID'###")
	print('###INITIAL_NUMBER###', var2)

	if type(var2) == int:
		if var2 % 2 == 0:
			print(var2, 'is int', 'also is an even number!')
		print(var2, 'converted to float', float(var2))
		print(var2, 'converted to complex', complex(var2))
		return(int(var2))

	elif type(var2) == float:
		print(round(var2, 2), 'is float // rounded "2 digits"')
		if round(var2, 0) % 2 == 0:
			print(round(var2, 2), 'converted to int', int(var2), 'also is an even number!')
		else:
			print(round(var2, 2), 'converted to int', int(var2), 'also is an odd number!')
		print(round(var2, 2), 'converted to complex', complex(var2))
		return(int(var2))

	else:
		print(var2, 'is complex')


converter_all(33.32)


print("###DONE!###")

sec = 24
print(type(sec))



	
	


