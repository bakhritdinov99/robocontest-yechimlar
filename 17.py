def summ(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s
def check(n):
    s=summ(int(n))
    return n%(s*s)==0
def get(n):
    r,x=0,0
    while r<n:
        x+=1
        if check(x):
            r+=1
    return x
n=input()
print(get(int(n)))