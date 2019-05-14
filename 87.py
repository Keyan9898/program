n,m=map(int,input().split())
if n>m:
x=n
else
x=m
for i in range(1,x+1):
	if n%i==0 and m%i==0:
		d=i
print(d)
