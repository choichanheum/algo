# Q17 - 경쟁적 전염
# N x N 크기의 시험관이 있다. 특정한 위치에 바이러스가 존재한다. 모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나이다.
# 모든 바이러스는 1초마다 상하좌우의 방향으로 증식한다. 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 또한 바이러스가 이미 존재하는 칸에 다른 바이러스는 들어갈 수 없다.
# 시험관 크기와 바이러스  정보가 주어졌을 때, S초가 지난 후 (x,y) 에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하라.
# https://www.acmicpc.net/problem/18405


'''
입력값
3 3
1 0 2
0 0 0
3 0 0
2 3 2

3 3
1 0 2
0 0 0
3 0 0
1 2 2

출력값
3

0
'''

import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

exam = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    exam[i][1:] = list(map(int, input().split()))

s, x, y = map(int, input().split())

virus = []

for i in range(1, n+1):
    for j in range(1, n+1):
        if exam[i][j] > 0:
            heapq.heappush(virus, (0, exam[i][j], i, j))

def infection(count, k, a, b):
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if nx>=1 and nx<=n and ny>=1 and ny<=n and exam[nx][ny]==0:
            exam[nx][ny] = k
            heapq.heappush(virus, (count+1, k, nx, ny))

result = []

while virus:
    count, k, a, b = heapq.heappop(virus)

    if count == s:
        break

    infection(count, k, a, b)

print(exam[x][y])

'''
책의 풀이는 최소힙 대신 리스트를 sort 후 큐에 넣어서 처리했음
'''