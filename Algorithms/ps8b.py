import random
import math


#print(list1)

def quickSort(arr, low, high):

	if low < high:
		k = math.floor((high-low)* 0.25) + high
		split1 = float(k) / len(arr)
		pi = quickselect(arr, low, high, split1);
		quickSort(arr, low, pi - 1);  #Before pi
		quickSort(arr, pi + 1, high); #After pi



# def quickselect(list1, left, right, k):
# 	#k = math.floor((len(list1)) * k)
# 	if left == right:
# 		return list1[left]

# 	split = partition(list1, left, right)

# 	length = split - left + 1

# 	if length == k:
# 		return list1[split]

# 	elif k < length:
# 		return quickselect(list1,left,split-1,k)

# 	else:
# 		return quickselect(list1, split+1, right, k-length)


def quickselect(a, low, high, split):
    k = math.floor((len(a)) * split)
    if low == high:
        return low
    pivotIndex = partition(a, low, high)
    if pivotIndex == k:
        return k
    elif pivotIndex > k:
        high = pivotIndex - 1
        return quickselect(a,low,high,split)
    else:
        low = pivotIndex + 1
        return quickselect(a,low,high,split)

def partition(list1, left, right):
	pivot = list1[left]
	leftMark = left + 1
	rightMark = right

	while True: #infintie while loop until breaks

		
		while leftMark < right and list1[leftMark] < pivot:
			leftMark +=1

		while rightMark > left and list1[rightMark] > pivot:
			rightMark -= 1

		if leftMark >= rightMark:
			break

		else:
			temp=list1[leftMark]
			list1[leftMark] = list1[rightMark]
			list1[rightMark] = temp

	temp=list1[left]
	list1[left] = list1[rightMark]
	list1[rightMark] = temp

	#print(list1)


	return rightMark

n = 10

list1 = []
for x in range(1,n):
	list1.append(x)
	
random.shuffle(list1)


ans = 0

#list1 = random.sample(range(0,10), 10)

print(ans, list1)

#print(quickselect(list1, 0, len(list1)-1,5))
quickSort(list1,0,len(list1)-1)

print(ans, list1)  



