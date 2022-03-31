x = input()
li = []
for j in x:
    li.append(j)

s = li.count('1')

ind = li.index('1')
sanoq=0
for y in range(ind,ind+s):
    if li[y]=='1':
        sanoq+=1

if sanoq==s:
    print('YES')
else:
    print('NO')
