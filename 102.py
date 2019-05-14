import math
def div(m12):
    if m12%2==0:
        return div(m12/2)
    else:
        return math.ceil(m12)
m1=int(input())    
print(div(m1)) 
