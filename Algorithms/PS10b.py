

def alignStrings(x, y, Cinsert, Cdelete, Csub):

    n=len(x)
    m=len(y)

    S=[[0 for p in range(m+1)] for q in range(n+1)]

    for i in range(n+1):

        for j in range(m+1):

            if i == 0:
                S[i][j] = j  

            elif j == 0:
                S[i][j] = i   

            elif x[i-1] == y[j-1]:
                S[i][j] = min(S[i][j-1]+Cinsert,S[i-1][j]+Cdelete,S[i-1][j-1])

            else:
                S[i][j] = min(S[i][j-1]+Cdelete,S[i-1][j]+Cdelete,S[i-1][j-1]+Csub)

    return S


def extractAlignment(S,x,y, cinsert, cdelete, csub):

	n=len(x)
	m=len(y)

	i = n
	j = m

	a = []

	while i >= 0 and j >= 0:
		if(S[i][j] == S[i-1][j-1] and S[i][j] == S[i-1][j] and S[i][j] == S[i][j-1]):
			i -= 1
			j -= 1
			a.append("no op")

		elif(S[i][j] == S[i-1][j-1]):
			i -= 1
			j -= 1
			
			a.append("no op")

		else:
			minval = min(S[i-1][j-1], S[i-1][j], S[i][j-1])
			if(S[i-1][j-1] == minval):
				print(S[i-1][j-1])
				print(minval)
				i -= 1
				j -= 1
				#sub
				a.append("sub")
			elif(S[i-1][j] == minval):
				i -= 1
				#insert
				a.append("insert")
			elif(S[i][j-1] == minval):
				j -= 1
				#delete
				a.append("delete")

	a.pop()	
	a.reverse()

	return a




###########################

x = "EXPONENTIAL"
y = "POLYNOMIAL"

x = "I hear the train a comin' it's rollin' round the bend  And I ain't seen the sunshine since I don't know when  I'm stuck in Folsom Prison and time keeps dragging on  But that train keeps a rollin' on down to San Antone.    When I was just a baby my mama told me son  Always be a good boy don't ever play with guns  But I shot a man in Reno just to watch him die  When I hear that whistle blowin' I hang my head and I cry.    I bet there's rich folks eatin' in a fancy dining car  They're probably drinkin' coffee and smokin' big cigars  But I know I had it comin' I know I can't be free  But them people keep a movin' that's what tortures me.    Well if they freed me from this prison if that railroad train was mine  I bet I'd move it on a little farther down the line  Far from Folsom Prison that's where I want to stay  And I'd let that lonesome whistle blow my blues away"
y = "I hear the train a-comin, it's rolling 'round the bend  And I ain't been kissed lord since I don't know when  The boys in Crescent City don't seem to know I'm here  That lonesome whistle seems to tell me, Sue, disappear    When I was just a baby my mama told me, Sue  When you're grown up I want that you should go and see and do  But I'm stuck in Crescent City just watching life mosey by  When I hear that whistle blowin', I hang my head and cry    I see the rich folks eatin' in that fancy dining car  They're probably having pheasant breast and eastern caviar  Now I ain't crying envy and I ain't crying me  It's just that they get to see things that I've never seen    If I owned that lonesome whistle, if that railroad train was mine  I bet I'd find a man a little farther down the line  Far from Crescent City is where I'd like to stay  And I'd let that lonesome whistle blow my blues away"

S = alignStrings(x, y,2,1,2)

print(S)

a = extractAlignment(S,x,y,1,1,1)

count = 0

for i in a:
	if(i=='no op'):
		count += 1

print(a)

print(len(a))
print(count)









