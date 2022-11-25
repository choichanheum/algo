# Q11 - 뱀
# 'Dummy'라는 도스 게임이 있다. 뱀이 나와서 기어 다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 기어다니다가 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝난다.
# NxN 정사각 보드 위에서 진행함.
# 규칙
#   1. 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
#   2. 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
#   3. 이동한 칸에 사과가 없다면, 몸 길이를 줄여서 꼬리가 위치한 칸을 비워준다. (몸 길이는 변하지 않는다.)
# 사과의 위치와 뱀의 이동 결로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
# https://www.acmicpc.net/problem/3190


'''
입력값
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

출력값
9

'''


n = int(input()) # 보드의 크기

k = int(input()) # 사과의 개수

board = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 사과의 위치를 1로 변경
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

# 시작 위치(1,1)를 9로 변경
a, b = 1, 1
board[a][b] = 9

# 상하좌우 정의
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

idx = 0

count = 0 # 시간
end = 0 # 종료 여부

# 사과를 먹었을 때 꼬리를 줄이기 위한 이동 경로 리스트
history = [(1,1)]

# 90도 회전 함수
def rotate(c):
    global idx
    if c == 'D': # 오른쪽
        idx += 1
        if idx == 4:
            idx = 0
    elif c == 'L': # 왼쪽
        idx -= 1
        if idx == -1:
            idx = 3
            
l = int(input()) # 뱀의 방향 변환 횟수

# 방향 변환 정보를 리스트에 저장
datas = []
for _ in range(l):
    x, c = input().split()
    datas.append((int(x), c))

# 방향 변환 정보 읽기
for data in datas:
    if end == 1:
        break

    x = data[0]
    c = data[1]

    # 시간이 x와 같아질 때까지 한칸 씩 이동
    while count<x:
        # 한 칸 이동 후 시간 1초 증가            
        nx = a + dx[idx]
        ny = b + dy[idx]

        count += 1

        if nx<1 or nx>n or ny<1 or ny>n or board[nx][ny]==9:
            end = 1
            break

        if board[nx][ny] == 0: # 사과가 없으면 꼬리를 지움
            tail_a, tail_b = history.pop(0)
            board[tail_a][tail_b] = 0

        board[nx][ny] = 9
        history.append((nx,ny))

        a = nx
        b = ny

    rotate(c) # x만큼 이동했으면 방향 변환
        
while end==0:
    # 한 칸 이동 후 시간 1초 증가            
    nx = a + dx[idx]
    ny = b + dy[idx]

    count += 1

    if nx<1 or nx>n or ny<1 or ny>n or board[nx][ny]==9:
        end = 1
        
    if board[nx][ny] == 0: # 사과가 없으면 꼬리를 지움
        tail_a, tail_b = history.pop(0)
        board[tail_a][tail_b] = 0

    board[nx][ny] = 9
    history.append((nx,ny))

    a = nx
    b = ny

if end == 1:
    print(count)


# 보드 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        print(board[i][j], end=' ')
    print()



'''
책의 풀이

n = int(input())
k = int(input())

data = [[0] * (n+1) for _ in range(n+1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로 (동,남,서,북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        dicrection = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    while 1:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1<=nx and nx<=n and 1<=ny and ny<=n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break

        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1

        if index < l and time == info[index][0] # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
'''