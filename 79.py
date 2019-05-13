import math
s1,m=map(int,raw_input().split())
p=s1*m
if math.sqrt(p).is_integer():
    print "yes"
else:
    print "no"
