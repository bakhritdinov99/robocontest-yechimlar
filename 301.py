n = int(input())
li = list(map(int,input().split()))
a= True
l_s = sorted(li)

for x in range(n):
    if li[x]!=l_s[x]:
        a=False
        break
if a:
    print('YES')
else:
    print('NO')
