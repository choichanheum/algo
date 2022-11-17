n = int(input())
for i in range(1, n+1):
  s = str(i)
  cnt = 0
  for x in s:
    if (x=='3')|(x=='6')|(x=='9'):
      cnt+=1
  if cnt ==0:
    print(i, end=' ')
  else:
    print('X'*cnt, end=' ')