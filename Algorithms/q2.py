def fun(n):

	if n > 1:
		for i in range(1,int(n)):
			print("hi", "hi")
		fun(n/4)
		fun(n/4)
		fun(n/4)


fun(4)