def change(n,v,r):
	d = [0]*r
	while (n>0):
		k = r
		while k>0 and v[k-1]<=n:
			k -= 1
		if k == r:
			return "No Solution"
		else:
			n=n-v[k]
			d[k] += 1
	return d


v=[100,50,25,10,5,1]
r = len(v)
print(change(76,v,r))
	