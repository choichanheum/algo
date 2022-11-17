d = [[] for _ in range(10)]

for i in range(10):
  d[i] = list(map(int, input().split()))

x = 1
y = 1

while 1:
  if((d[x][y] == 2) | ((d[x][y+1] == 1) & (d[x+1][y] == 1))):
    d[x][y]=9
    break
  elif(d[x][y+1] == 0):
    d[x][y]=9
    y+=1
  elif(d[x][y+1] == 1):
    d[x][y]=9
    x+=1
  elif(d[x][y+1] == 2):
    d[x][y]=9
    d[x][y+1]=9
    break

for i in range(10):
  for j in range(10):
    print(d[i][j], end=' ')
  print()