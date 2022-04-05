s = input()
al = list(map(chr, range(97, 123)))+list(map(chr,range(65,91)))
soni = []
for x in al:
    soni.append(s.count(x))
for x in range(len(al)):
    print(al[x],soni[x])