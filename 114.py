a, b, c, d = map(int, input().split())
if a == b and b == c and c == d:
    print('YES')
elif b==d:
    print('NO')
else:
    N = (a - c) / (d - b)
    n = int(N)
    if N < 0:
        print('NO')
    elif N == n:
        print('YES')
    else:
        print('NO')
