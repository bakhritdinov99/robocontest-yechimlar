n = int(input())
s=0
if n>0:
    for x in range(1, n + 1):
        s += x
else:
    for x in range(1, n - 1,-1):
        s += x
print(s)