def hindex(arr):

	hindexnum = 0

	if(arr is None):
		return 0

	for i in range(1, len(arr)):
		count = 0
		for j in arr:
			if(j>=i):
				count += 1
		if(count >= i):
			hindexnum += 1

	return hindexnum

#do you have x number of papers that are cited x times?



citations = [6,5,3,1,0]

print(hindex(citations))