a,b = map(int,input().split())

ua = (a+b)/2
ug = pow(a*b,0.5)

if ua>ug:
    print('>')
elif ua==ug:
    print('=')
else:
    print('<')