n=int(input())
s1=(n//10)*2
s2=n%10
if s2>2 and s2<7:
    s1+=1
elif s2>6:
    s1+=2
print(s1)