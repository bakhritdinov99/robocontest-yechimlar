n,k=map(int,input().split())
mod=pow(10,9)+7
if n==0:
    print('0')
else:
    s=((pow(k,n)-1)//(k-1))%mod
    print(s)