n = input()
son = []
uzun = len(n)

for x in range(uzun):
    son.append(n[x])

for x in range(uzun):
        if son[x]=='1':
            son[x]='bir'
        elif son[x]=='2':
            son[x]='ikki'
        elif son[x]=='3':
            son[x]='uch'
        elif son[x]=='4':
            son[x]='to\'rt'
        elif son[x]=='5':
            son[x]='besh'
        elif son[x]=='6':
            son[x]='olti'
        elif son[x]=='7':
            son[x]='yetti'
        elif son[x]=='8':
            son[x]='sakkiz'
        elif son[x]=='9':
            son[x]='to\'qqiz'
son.reverse()

def unlik(m):
    for x in range(1,len(m),3):
        if son[x] == 'bir':
            son[x] = 'o\'n'
        elif son[x] == 'ikki':
            son[x] = 'yigirma'
        elif son[x] == 'uch':
            son[x] = 'o\'ttiz'
        elif son[x] == 'to\'rt':
            son[x] = 'qirq'
        elif son[x] == 'besh':
            son[x] = 'ellik'
        elif son[x] == 'olti':
            son[x] = 'oltmish'
        elif son[x] == 'yetti':
            son[x] = 'yetmish'
        elif son[x] == 'sakkiz':
            son[x] = 'sakson'
        elif son[x] == 'to\'qqiz':
            son[x] = 'to\'qson'

    for x in range(2, len(m), 3):
        if son[x]!='0':
            son[x]+=' yuz'

    for x in range(3,len(m),3):
        if x//3==1:
            son[x] += ' ming'
        if x // 3 == 2:
            son[x] += ' million'
        if x // 3 == 3:
            son[x] += ' milliard'

unlik(son)
son.reverse()

for x in range(len(son)):
    if son[x]=='0 ming':
        son[x]='ming'
    if son[x]=='0 yuz':
        son[x]='yuz'
    if son[x]=='0 million':
        son[x]='million'
    if son[x]=='0 milliard':
        son[x]='milliard'

k=0
for x in son:
    if x=='0':
        k+=1

for x in range(k):
    son.remove('0')

umu=''
for x in son:
    umu+=x+' '

print(umu)