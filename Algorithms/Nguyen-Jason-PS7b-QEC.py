import random

def make(n):
	Arr1 = []
	Arr2 = []
	for x in range(0,n):
		Arr1.append('{0}'.format(x))
		Arr2.append('{0}'.format(x))
	random.shuffle(Arr1)
	random.shuffle(Arr2)
	return Arr1, Arr2

def matchpairs(Arr1, Arr2, low, high):
	if(low<high):
		pivot = partition(Arr1, low, high, Arr2[high])

		partition(Arr2, low, high, Arr1[pivot])

		matchpairs(Arr1, Arr2, low, pivot-1); 
		matchpairs(Arr1, Arr2, pivot+1, high); 

	return Arr1, Arr2

def partition(arr, low, high, pivot):
	i = low
	temp1 = temp2 = ''
	
	for x in range(low, high):
		if(arr[x]<pivot):
			temp1 = arr[i]
			arr[i] = arr[x]
			arr[x] = temp1
		elif(arr[x]==pivot):
			temp1 = arr[x]
			arr[x] = arr[high]
			arr[high] = temp1
			x -= 1
	temp2 = arr[i]
	arr[i] = arr[high]
	arr[high] = temp2

	return i

Arr1, Arr2 = make(100)

Arr1, Arr2 = matchpairs(Arr1, Arr2, 0, 99)

for x in range(0, len(Arr1)):
	if Arr1[x]!=Arr2[x]:
		print("Broken!")

print("If program ran without saying 'Broken' then both arrays are sorted!")





