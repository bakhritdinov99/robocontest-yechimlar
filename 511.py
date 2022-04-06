s =input()
if int(s)>=0 or len(s)==2:
    print(s)
else:
    print(int(s[:2])+int(s[2:]))