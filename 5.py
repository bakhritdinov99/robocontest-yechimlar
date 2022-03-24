from math import sqrt
f=int(input())
k=0
z=abs(f)
i=int(sqrt(z))
if z==0:
    print('-1')
else:
    for x in range(1,i+1):
        if abs(z)%x==0:
            k+=1
    k*=2
    if f<0 and int(sqrt(z))==sqrt(z):
        print(k-1)
    else:
        print(k)