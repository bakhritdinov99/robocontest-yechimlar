n=int(input())
x=n%100
y=n-x
z=x//2
na=y+z
ya=n-50
na2=ya-z
if na>na2:
    print(na2,na)
else:
    print(na,na2)