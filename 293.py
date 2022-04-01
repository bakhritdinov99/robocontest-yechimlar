a = input()
def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m


t = toBinary(a)
print(len(a))
for x in t:
    print(x)