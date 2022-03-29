n = int(input())

l = []
g=[]

i=1
q=n*1000
while i<q:
    l.append(i)
    i+=1

def raq_yig(r):
    s=0
    while r:
        s+=r%10
        r//=10
    return s

j=1
while j<q:
    if j%pow(raq_yig(j),2)==0:
        g.append(j)
    j+=1
if n==1:
    print(1)
elif n==2:
    print(10)
elif n==3:
    print(20)
else:
    print(g[n-1])