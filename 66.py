num3= int(raw_input())
for j in range(2, int(num3/2)):
    if num3 % j  == 0:
        print("no")
        break
else:
    print("yes")
