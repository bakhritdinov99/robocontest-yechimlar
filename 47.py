x=int(input())
array=[]
arr=[]
san=[]
for i in range(x):
    s=int(input())
    array.append(s)
    j = 0
    x=0
    while array[i]>0:
        q = array[i] % 2
        array[i] = array[i] // 2
        arr.append(q)
        if arr[j] == 1:
            x+=1
        j+=1
    arr.clear()
    san.append(x)
d=len(san)
for i in range(d):
    print(san[i],' ')