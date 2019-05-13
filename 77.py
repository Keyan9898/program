m=int(input(""))
l=[]
for i in range(1,m+1):
  if m%i==0:
    l.append(i)
print(*l,end="")
