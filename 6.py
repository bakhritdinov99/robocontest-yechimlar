yil = int(input())
if yil%400==0 or (yil%4==0 and yil%100!=0):
    kun='12'
else:
    kun='13'

if len(str(yil))==4:
    print(f"{kun}/09/{yil}")
elif len(str(yil))==3:
    print(f"{kun}/09/0{yil}")
elif len(str(yil))==2:
    print(f"{kun}/09/00{yil}")
elif len(str(yil))==1:
    print(f"{kun}/09/000{yil}")