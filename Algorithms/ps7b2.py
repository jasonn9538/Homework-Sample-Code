import numpy as np 
import random

def make(n):
	Arr = []
	for x in range(1,n+1):
		Arr.append(x)
	random.shuffle(Arr)
	return Arr

def insertSort(arr):

	flips = 0

	for i in range(0,len(arr)):
		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] : 
			arr[j + 1] = arr[j] 
			j -= 1
			flips += 1
		arr[j + 1] = key

	return arr, flips

def mergeSort(arr):

    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid]
        R = arr[mid:]
  
        a, ai = mergeSort(L)
        b, bi = mergeSort(R) 
  
        i = j = k = 0

        flips = 0 + ai + bi
         
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
                flips += (len(a)-i) 
                #iterator i tracks hor many elements in a have been 
                #appended to c. Therefore, if we substract i from len(a).
                #We get the # of flips involving b
            k+=1
          
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1

        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    else:
    	return arr, 0
            
            
    return arr, flips

def mergeSortCount(arr): #this is just to test my correctness. Code was taken from geeksforgeeks
    inv_count = 0
    n = len(arr)
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count 


# TEST CODE, PLEASE IGNORE
#testarr = [1, 3, 5, 2, 4, 6]
# testarr = make(10)
# print(testarr)
# print(mergeSortCount(testarr))
# print(mergeSort(testarr))


testvals = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

insertSortflips = []

mergeSortflips = []

for x in testvals:
	arr = make(x)
	
	x, y = insertSort(arr)
	
	insertSortflips.append(y)


for x in testvals:
	arr = make(x)
	
	x, y = mergeSort(arr)
	
	mergeSortflips.append(y)

print(insertSortflips)

print(mergeSortflips)












		

