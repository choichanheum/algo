# Q15 - 특정 거리의 도시 찾기
# 어떤 나라에 1~N번 까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
# 이때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시의 번호를 출력하라. 또한 X에서 X로 가는 최단 거리는 항상 0이라고 가정한다.
# https://www.acmicpc.net/problem/18352


'''
입력값
4 4 2 1
1 2
1 3
2 3
2 4

출력값
4

'''

from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

distance = [-1 for _ in range(n+1)]

distance[x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([x])

while q:
    now = q.popleft()

    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)

exists = False

for i in range(1, n+1):
    if distance[i] == k:
        exists = True
        print(i)
    
if not exists:
    print(-1)