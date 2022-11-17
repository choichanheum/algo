a, d, n = input().split()

a = int(a)
d = int(d)
n = int(n)

for i in range(n):
  if i==n-1:
    print(a)
  a+=d