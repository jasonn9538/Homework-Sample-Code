A = [4,2,7,3,6,9,10] 

def sorting(A):

	for i in range(0,len(A)-1):

		for j in range(0,len(A)-i-1):

			if A[j+1] < A[j]:

				A[j+1], A[j] = A[j], A[j+1] 

	return A

print(sorting(A))



