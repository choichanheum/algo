h, w = input().split()
h = int(h)
w = int(w)

pan = [[0 for _ in range(w)] for _ in range(h)]

n = int(input())

for _ in range(n):
  l, d, x, y = input().split()
  l = int(l)
  d = int(d)
  x = int(x)-1
  y = int(y)-1

  if d==0:
    for i in range(y, y+l):
      pan[x][i] = 1
  elif d==1:
    for i in range(x, x+l):
      pan[i][y] = 1

for i in range(h):
  for j in range(w):
    print(pan[i][j], end=' ')
  print()