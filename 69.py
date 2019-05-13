class ifoddeve:
	def sub(self,n,j):
		s=n-j
		s=abs(s)
		if s%2==0:
			print("even")
		else:
			print("odd")
n,j=map(int,input().split())
call=ifoddeve()
call.sub(n,j)
