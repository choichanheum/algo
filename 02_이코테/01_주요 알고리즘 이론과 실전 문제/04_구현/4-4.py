# 구현 예제 4-4. 게임 개발 (실전)
# NxM 크기의 직사각형 맵 안에서 캐릭터가 매뉴얼에 따라 이동한 뒤, 캐릭터가 방문한 칸의 수를 출력하라.
# 각각의 칸은 육지 또는 바다이며, 바다는 갈 수 없다.
# 1. 현재 방향을 기준으로 왼쪽(반시계90도 회전)방향 부터 차례대로 갈 곳을 정함
# 2. 왼쪽 방향에 가보지 않은 칸이 존재하면, 왼쪽 방향으로 회전한 다음 앞으로 한 칸 전진한다. 만약 가보지 않은 칸이 없으면 방향 회전만 수행한다.
# 3. 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 경우 바라보는 방향을 유지한채로 뒤로 한 칸 이동한다. 만약 뒤쪽 방향이 바다여서 이동불가한 경우 움직임을 멈춘다.
# 방향 d = [ 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽 ]
# 0 : 육지, 1 : 바다

'''
입력값
4 4       # 4 x 4 맵 생성
1 1 0     # (1, 1) 에 북쪽(0)을 바라보고 서 있는 캐릭터
1 1 1 1   #   첫 줄은 모두 바다
1 0 0 1   # 둘째 줄은 바다/육지/육지/바다
1 1 0 1   # 셋재 줄은 바다/바다/육지/바다
1 1 1 1   # 넷재 줄은 모두 바다

출력값
3
'''

n, m = map(int, input().split())
pan = [[0]*m for _ in range(n)]
a, b, d = map(int, input().split())

for i in range(n):
    pan[i] = list(map(int, input().split()))

print()
print()

pan[a][b] = 9

for i in range(n):
    for j in range(m):
        print(pan[i][j], end=' ')
    print()

print("d=",d)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r_count = 0

while 1:
    d -= 1
    if d == -1:
        d = 3

    if pan[a+dx[d]][b+dy[d]] == 0:
        a += dx[d]
        b += dy[d]
        pan[a][b] = 9
        r_count = 0
        continue
    else:
        r_count += 1
    
    if r_count == 4:
        if pan[a-dx[d]][b-dy[d]] == 0:
            a -= dx[d]
            b -= dy[d]
            r_count = 0
        else:
            break

print()
print()

pan[a][b] = 9

for i in range(n):
    for j in range(m):
        print(pan[i][j], end=' ')
    print()

print("d=",d)

result = 0

for i in range(n):
    result += pan[i].count(9)

print(result)