
x=int(input())
mass=[]
for i in range(x):
    a,b=map(int,input().split())
    if b==((1+a)*a)/2:
        mass.append(1)
    else:
        mass.append(0)

for i in range(x):
    print(mass[i],end='')
