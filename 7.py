fib1 = 2
fib2 = 4
n = int(input())
i = 0
if n<=0:
    print(0)
elif n==1 or n==2:
    print(2)
else:
    n=n-1
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    print(fib2)