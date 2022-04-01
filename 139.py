n = int(input())
to = list(map(int,input().split()))

b = 0
i = 0
u = 0
t = 0
be = 0

for x in to:
    if x==1:
        b+=1
    elif x==2:
        i+=1
    elif x==3:
        u+=1
    elif x==4:
        t+=1
    else:
        be+=1


ma = max(b,i,u,t,be)

if b==ma:
    print('1')
elif i==ma:
    print('2')
elif u==ma:
    print('3')
elif t==ma:
    print('4')
else:
    print('5')