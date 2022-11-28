# Q16 - 연구소
# 연구소에서 바이러스가 유출되었다. 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해 연구소에 벽을 세우려고 한다.
# 연구소는 크기가 N x M 이다. 연구소는 빈칸, 벽으로 이루어지고, 일부 칸에는 바이러스가 존재한다. 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있다.
# 새로 3개의 벽을 세운다고 할 때, 안전 영역 크기의 최댓값을 구하라.
# https://www.acmicpc.net/problem/14502


'''
입력값
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

출력값
27

'''

import sys
from itertools import combinations
import copy

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())

lab = []
virus = []
empty = []

for _ in range(n):
    lab.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            virus.append((i,j))
        elif lab[i][j] == 0:
            empty.append((i,j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 바이러스 확산
def infection(array, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx>=0 and nx<n and ny>=0 and ny<m:
            if array[nx][ny] == 0:
                array[nx][ny] = 2
                infection(array, nx, ny)

# 배열의 현재 안전 영역의 크기 확인
def get_size(array):
    size = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                size += 1
    return size

result = 0

# 벽3개를 세우는 모든 경우의 수
cases = list(combinations(empty, 3))

for case in cases:
    # 연구소 원본을 복사하여 temp 생성
    temp = copy.deepcopy(lab)

    # temp에 벽 세우기
    for x, y in case:
        temp[x][y] = 1

    # temp에 바이러스 확산시키기
    for x, y in virus:
        infection(temp, x, y)

    # 현재 안전 영역 크기 확인해서 result 갱신
    result = max(result, get_size(temp))

print(result)