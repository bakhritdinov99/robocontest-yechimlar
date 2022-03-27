N,K=map(int,input().split())

def pow_mod(x, y, z):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number
b=10**9+7
x=pow_mod(K+1,N-1,b)

if N==0:
    print(1)
else:
    print(x)

