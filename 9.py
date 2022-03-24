n=int(input())
li=list(map(int,input().split()))

for x in range(n):
    y=li[x]
    if li.count(y)==1:
        print(y)