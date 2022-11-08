# DFS/BFS 예제 5-11. 미로 탈출 (실전)
# N x M 크기의 직사각형 미로에서 탈출해야함. 괴물이 있는 부분은 0, 없는 부분은 1로  표시.
# 시작 위치는 (1,1) 이고 출구는 (N,M) 이다.
# 탈출하기 위해 움직여야하는 최소 칸의 개수를 구하라.

'''
입력값
5 6
101010
111111
000001
111111
111111


출력값
10
'''

from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx >=n or ny<0 or ny>=m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))

for i in range(n):
    for j in range(m):
        print(graph[i][j], end = ' ')
    print()