x=int(input())
ma=[]
if x>0:
    while x>0:
        q=x%2
        x=x//2
        ma.append(q)
elif x<0:
    x=4294967296+x
    while x>0:
        q=x%2
        x=x//2
        ma.append(q)
ma.reverse()
d=len(ma)
for x in range(32-d):
    print('0',end='')
for i in range(d):
    print(ma[i],end='')