def function(c, step):
	for i in range(0, c, step):
		if i % 2 == 0:
			print(i)
			continue
		else:
			print(i, 'uneven')
			break
	


c = 40
step = 3

function(c, step)