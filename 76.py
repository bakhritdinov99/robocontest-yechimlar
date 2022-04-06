a, b, c, d, e, f, g = map(int, input().split())
S = int(input())
y = a + b + c + d + e + f + g

if S-y>=0:
    print(S-y)
else:
    print(0)
