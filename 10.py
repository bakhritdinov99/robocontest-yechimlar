N=int(input())
a,b,c=map(int,input().split())
if N<=a+b+c:
    print('Yes')
else:
    print('No')