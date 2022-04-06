x=int(input())
arr=[]
nat=[]
for i in range(x):
    d=int(input())
    arr.append(d)

for i in range(x):
    y=arr[i]*arr[i]*arr[i]+arr[i]
    print(y)
