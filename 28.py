n=int(input())
arr=[]
for i in range(n):
    s=list(map(int,input().split()))
    arr.append(s)
for i in range(n):
    print(2*arr[i][2]-arr[i][0],2*arr[i][3]-arr[i][1])