import time

def top_down(n): #part a

	if(n==0):
		return 1
	if(n==1):
		return 1

	pn=2*(top_down(n-1))+top_down(n-2)

	return pn

#creating an array for memoization for part b to fill from top to bottom
MAX = 100
f_td = [0] * MAX
def dynamprog_topdown(n): #part b
	if(n==0):
		f_td[0] = 1
	if(n==1):
		f_td[1] = 1

	if(f_td[n]):
		return f_td[n]	

	f_td[n] = 2*dynamprog_topdown(n-1)+dynamprog_topdown(n-2)

	return f_td[n]


#creating an array for memoization for part c to fill from bottom to top
MAX = 100
f_bu = [0] * MAX

def dynamprog_bottomup(n): #part c
	
	f_bu[0]=1
	f_bu[1]=1

	if(f_bu[n]):
		return f_bu[n]

	for i in range(2,n+1):
		f_bu[i]=2*(f_bu[i-1])+f_bu[i-2]

	return f_bu[n]


def dynamprog_bottomup1(n): #part c
	
	p0=1
	p1=1

	if(n==0):
		return 1
	if(n==1):
		return 1

	for i in range(2,n+1):
		temp = 2*(p1)+p0
		p0 = p1
		p1 = temp


	return temp

#################################
## TESTING CODE
#################################

times = []

n=10

print(dynamprog_bottomup1(n))

print("Dynamic Programming/Top Down(part b): {}".format(dynamprog_topdown(n)))

# jobtime = time.time()

# print("Top down(part a): {}".format(top_down(n)))

# newjobtime = time.time() - jobtime 

# print(newjobtime)

# times.append(newjobtime)

# jobtime = time.time()

# print("Dynamic Programming/Top Down(part b): {}".format(dynamprog_topdown(n)))

# newjobtime = time.time() - jobtime 

# print(newjobtime)

# times.append(newjobtime)

# jobtime = time.time()

# print("Dynamic Programming/Bottom Up(part c): {}".format(dynamprog_bottomup(n)))

# newjobtime = time.time() - jobtime 

# print(newjobtime)

# times.append(newjobtime)

# print(times)

# #print(dynamprog())

# bottomuptimes = []
# topdowntimes = []
# totalbottomuptime = 0
# totaltopdowntime = 0

# numofruns = 1000000

# for x in range(0,numofruns):
	
# 	MAX = 100
# 	f_bu = [0] * MAX

# 	jobtime = time.time()

# 	dynamprog_bottomup(n)

# 	newjobtime = time.time() - jobtime 

# 	totalbottomuptime += newjobtime

# 	bottomuptimes.append(newjobtime)

# print("bottomuptimes")
# #print(bottomuptimes)
# print(totalbottomuptime/numofruns)

# for x in range(0,numofruns):
	
# 	MAX = 100
# 	f_td = [0] * MAX

# 	jobtime = time.time()

# 	dynamprog_topdown(n)

# 	newjobtime = time.time() - jobtime 

# 	totaltopdowntime += newjobtime

# 	topdowntimes.append(newjobtime)

# print("topdowntimes")
# #print(bottomuptimes)
# print(totaltopdowntime/numofruns)


