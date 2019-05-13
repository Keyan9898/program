def odddig():
	m=int(input())
	p1=[]
	while(m!=0):
		p1.append(m%10)
		n//=10
	for i in range(len(p1)-1,-1,-1):
		if p1[i]%2!=0:
			print(p1[i]),
try:
	odddig()
except:
	print('invalid')
