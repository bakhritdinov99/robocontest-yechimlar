n=int(input())

if n>12:
    print('Error')
else:
    if n==1 or n==12 or n==2:
        print('Winter')
    elif n>2 and n<6:
        print('Spring')
    elif n>5 and n<9:
        print('Summer')
    else:
        print('Autumn')