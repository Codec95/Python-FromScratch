
def fib(n):
	if n < 2:
		print('first', n)
		return n
	else:
		print('second', n)
		return fib(n-1)+fib(n-2)

num = fib(10)
print(num)