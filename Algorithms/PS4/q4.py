import random
import numpy as np
import collections
import matplotlib.pyplot as plt


def getMaxOccuringChar(data):

	return collections.Counter(data).most_common(1)

def createKey():

	key = []

	for i in range(0,26):
		key.append(random.randint(0,10000))


	return key

def letterIndex(letter):
	alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
			 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
			 'U', 'V', 'W', 'X', 'Y', 'Z']

	for i in range(0,26):
		if alpha[i] == letter:
			return (i+1)
	print("something went wrong")
	return "BROKEN"


def importdata():
	f = open("names.txt", "r")
	f = f.readlines()

	newf = []

	for lines in f:
		temp = lines.split('\t')
		newf.append(temp[0])


	random.shuffle(newf)

	newf = newf[:(len(newf)//10)]

	return newf

data = importdata()



finaldata = []
chainLength = []

key = [1358, 8873, 2733, 552, 2509, 1663, 4048, 1082, 5967, 8270, 2672, 2811, 5812, 1239, 581, 3625, 4544, 2744, 3622, 6330, 6300, 3737, 1555, 6378, 7175, 2154]

counts = 0

for l in range(1,400):
	finaldata = []
	for i in data:
		hashnumber = 0
		for j in i:
			number = letterIndex(j)
			hashnumber += (number) 
		finaldata.append(hashnumber%l)

		# #finding the maximum chain length
		# chainLengthNum = getMaxOccuringChar(finaldata)[:1][0][1]
		# print(chainLengthNum)

		# #counter to see check progress while running
		# counts += 1 
		# print(len(data)-counts)

		

	chainLengthNum = getMaxOccuringChar(finaldata)[:1][0][1]
	print(chainLengthNum, l)
	#appending chain length onto a list
	chainLength.append(chainLengthNum)




# print(chainLength)

## CODE FOR PLOT 
x = range(0, len(chainLength))
plt.plot(x,chainLength)
plt.show()
######################

#CODE FOR HISTOGRAM
# plt.hist(finaldata, bins=500)
# plt.show()
########################



