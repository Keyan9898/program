str12=input()
if (len(str12)%2==0):
    m=len(str12)//2
    print(str12[:m-1]+'*'+'*'+str12[m+1:])
else:
    m=len(str12)//2
    print(str12[:m]+'*'+str12[m+1:])
