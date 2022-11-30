# Q20 - 감시 피하기
# NxN 크기의 복도가 있다. 특정한 위치에는 선생님, 학생, 혹은 장애물이 위치할 수 있다. 학생들은 선생님의 감시에 들키지 않는 것이 목표이다.
# 각 선생님들은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시를 진행한다. 단, 복도에 장애물이 위치한 경우, 선생님은 장애물 뒤편에 숨어 있는 학생들은 볼 수 없다.
# 또한 선생님은 상, 하, 좌, 우 4가지 방향에 대하여, 아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다고 가정하자.
# 해당 위치에 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X가 주어진다.
# NxN 크기의 복도에서 학생 및 선생님의 위치 정보가 주어졌을 때, 장애물을 정확히 3개 설치하여 모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 출력하는 프로그램을 작성하라.
# 모든 학생들을 감시로부터 피하도록 할 수 있다면 "YES", 그렇지 않다면 "NO"를 출력한다.
# https://acmicpc.net/problem/18428

'''
입력값
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

4
S S S T
X X X X
X X X X
T T T X

출력값
YES

NO

'''

from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())

hall = []
teachers = []
spaces = []

for _ in range(n):
    hall.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if hall[i][j] == "T":
            teachers.append((i, j))
        if hall[i][j] == "X":
            spaces.append((i, j))

def watch():
    global success

    for x, y in teachers:

        for i in range(4):
            nx = x
            ny = y
            while 1:
                if i == 0: # 상
                    nx -= 1
                elif i == 1: # 하
                    nx += 1
                elif i == 2: # 좌
                    ny -= 1
                elif i == 3: # 우
                    ny += 1

                if nx<0 or nx>=n or ny<0 or ny>=n or hall[nx][ny] == "O":
                    break

                if hall[nx][ny] == "S":
                    return True
            
    return False

success = False

for obstacles in combinations(spaces, 3): # 빈공간 중 장애물을 설치할 3곳을 선택하는 경우의 수(조합)
    
    for obs_x, obs_y in obstacles:
        hall[obs_x][obs_y] = "O"

    if not watch(): # 모든 case를 감시해서 학생을 발견하지 못한 경우
        success = True
        break

    for obs_x, obs_y in obstacles:
        hall[obs_x][obs_y] = "X"

print("YES" if success else "NO")