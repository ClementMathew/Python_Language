for i in range(1,1000):
	if(i>1):	
		for j in range(2,i):
			if(i%j) == 0:
				break
		else:
			print(i)
