a1,a2,a3 = map(int,input().split())
b1,b2,b3 = map(int,input().split())

s=(b1-a1)*3600+(b2-a2)*60+(b3-a3)
print(s)