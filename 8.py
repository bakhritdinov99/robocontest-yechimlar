a,b,c,d,e=map(int,input().split())
mi=min(a,b,c,d,e)
ma=max(a,b,c,d,e)
print(a+b+c+d+e-ma, a+b+c+d+e-mi)