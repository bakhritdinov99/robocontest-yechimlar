n = int(input())
li = list(map(int,input().split()))

son = []

for x in range(1,101):
    son.append(li.count(x))
ma = max(son)
print(n-ma)

