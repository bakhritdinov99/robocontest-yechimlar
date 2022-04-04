n=input()
li = []
if len(n) == 6 :
    for x in n:
        li.append(int(x))
    if li[0]+li[1]+li[2] == li[3]+li[4]+li[5]:
        print('YES')
    else:
        print('NO')
else:
    print('NO')