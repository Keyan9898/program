m=int(input())
prod=1
k=0
while(m):
    k=m%10
    prod=prod*k
    m=m//10
print(prod)
