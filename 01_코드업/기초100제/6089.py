a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

for i in range(n):
  if i==n-1:
    print(a)
  a*=r