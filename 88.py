m12,m22=map(int,input().split())
if m12>m22:
min1=m12
else:
min1=m22
while(l):
if((min1%m12)==0 and(min1%m22)==0):
print(min1)
break
min1=min1+1
