# Q19 - 연산자 끼워 넣기
# 
# https://acmicpc.net/problem/14888


'''
입력값
2
5 6
0 0 1 0

3
3 4 5
1 0 1 0

6
1 2 3 4 5 6
2 1 1 1

출력값
30
30

35
17

54
-24

'''
import sys
input = sys.stdin.readline

n = int(input())

sequence = list(map(int, input().split()))

plus, minus, multi, div = map(int, input().split())

max_value = int(-1e9)
min_value = int(1e9)

def dfs(i, now):
    global plus, minus, multi, div, max_value, min_value
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, now + sequence[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, now - sequence[i])
            minus += 1
        if multi > 0:
            multi -= 1
            dfs(i+1, now * sequence[i])
            multi += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / sequence[i]))
            div += 1

dfs(1, sequence[0])

print(max_value)
print(min_value)