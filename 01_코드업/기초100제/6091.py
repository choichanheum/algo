a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

d = 1

while (d%a!=0) | (d%b!=0) | (d%c!=0):
  d += 1

print(d)