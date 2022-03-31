x = int(input())
soat= x//3600

so = soat//24
s = soat-so*24
m = x-x//3600*3600
min = m//60

se = x-x//3600*3600-m//60*60

def nolqush(x):
    if x < 10:
        x = str(x)
        x = '0' + x
    return x

min = nolqush(min)
se = nolqush(se)
print(f"{s}:{min}:{se}")
