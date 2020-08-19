


# def maxprotein(p, c, maxC):

# 	dp = [0] * (len(p)+1)

# 	ans = 0

# 	for i in range(0,maxC+1):
# 		for j in range(len(p)):
# 			if (c[j]<= i):
# 				dp[i] = max(dp[i], dp[i - c[j]] + p[j]) 

# 	return dp[maxC]




def maxprotein(maxC, p, c): 
  
    n = len(p)

    dp = [0 for i in range(maxC + 1)] 
  
    ans = 0

    for i in range(maxC + 1): 
        for j in range(n): 
            if (c[j] <= i): 
                dp[i] = max(dp[i], dp[i - c[j]] + p[j]) 
    print(dp)

    return dp[maxC]





p = [4, 6, 7, 2, 1] #protein
c = [20, 15, 28, 100, 1] #calories
n = len(p)
maxC = 100

print(maxprotein(maxC,p,c))

#print(unboundedKnapsack(maxC,n,p,c))