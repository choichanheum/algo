# 구현 예제 4-1. 상하좌우
# 여행가 A 가 NxN 의 정사각형 공간에서 (L,R,U,D)의 방향으로 이동할 수 있는데, 계획서가 주어졌을 때 A가 최종적으로 도착할 지점의 좌표를 출력하라.
# 시작은 (1,1) 마지막은 (n,n) 이며 공간을 벗어나는 움직임은 무시한다.

'''
입력값
5
R R R U D D

출력값
3 4
'''

n = int(input())

plans = input().split()

x, y = 1, 1

for plan in plans:
    print(plan)
    if plan == 'L' and y > 1:
        y -= 1
    elif plan == 'R' and y < n:
        y += 1
    elif plan == 'U' and x > 1:
        x -= 1
    elif plan == 'D' and x < n:
        x += 1

print(x, y)