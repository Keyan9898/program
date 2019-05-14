n,m=map(int,input().split())
l=list(map(int,input().split()))
g=[]
for i in l:
	if i%2==1:
		g.append(i)
print(g[m-1])
