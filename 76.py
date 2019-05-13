m1=int(raw_input())
factor=0
for i in range(1,m1):
  if m1%i==0:
    factor=i
if factor>1:
  print "yes"
elif m1==1:
  print "prime"
else:
  print "no"
