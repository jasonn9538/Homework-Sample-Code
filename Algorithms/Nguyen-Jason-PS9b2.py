
MAX = 100
maxArrEven = [0] * MAX
maxArrOdd = [0] * MAX

def maxPoints(arr):

	n = len(arr)

	maxArr = [0] * n

	maxArr[0] = arr[0]
	maxArr[1] = max(arr[0],arr[1])

	print(maxArr)

	for i in range(2,n):
		maxArr[i] = max(maxArr[i-1], maxArr[i-2]+arr[i])
		print(i)
		print(maxArr)

	return maxArr[n-1]


def maxPointsPartB(arr):

	n = len(arr)

	max1 = arr[0]
	max2 = max(arr[0],arr[1])

	for i in range(2,n):
		tempMax = max(max2, max1+arr[i])
		max1 = max2
		max2 = tempMax

	return tempMax


arr = [1,7,3,5,10]

print(maxPoints(arr))

print(maxPointsPartB(arr))