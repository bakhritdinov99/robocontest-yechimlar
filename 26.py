n=int(input())
mod = 1000000007
la=[]
for x in range(n):
   la.append(int(input()))

ls= []

for x in la:
    ls.append(x*x%mod)

for x in ls:
    print(x)