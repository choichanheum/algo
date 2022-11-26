# Q12 - 기둥과 보 설치
# 벽면의 크기 n, 기둥과 보를 설치하거나 삭제하는 작업이 순서대로 담긴 2차원 배열 build_frame 이 매개변수로 주어질 때, 모든 명령어를 수행한 후 구조물의 상태를 return하라.
# 규칙
#   1. 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
#   2. 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
# build_frame = [x, y, a, b]
#   x,y는 좌표
#   a는 종류 (0: 기둥, 1: 보)
#   b는 설치/삭제 여부 (0: 삭제, 1: 설치)
# 구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제합니다.
# return = [x, y, a]  -> 정렬기준 : 1. x좌표 기준 오름차순 정렬, 2. y좌표 기준 오름차순 정렬, 3. 기둥, 보
#   x,y는 좌표
#   a는 종류 (0: 기둥, 1: 보)
# https://programmers.co.kr/learn/courses/30/lessons/60061


'''
입력값
5
[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

5
[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]


출력값
[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

'''

# 설치/삭제한 구조물이 규칙을 위반하지 않는지 체크 (위반 시 False 리턴)
def check(answer):
    for data in answer:
        x, y, a = data
        if a == 0: # 기둥
            # 1. 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False

        if a == 1: # 보
            # 2. 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False

    return True

def solution(n, build_frame):
    answer = []

    for data in build_frame:
        x, y, a, b = data

        if b == 0: # 삭제
            answer.remove([x, y, a])
            if not check(answer): # 규칙을 위반하지 않는지 체크
                answer.append([x, y, a])
        
        if b == 1: # 설치
            answer.append([x, y, a])
            if not check(answer): # 규칙을 위반하지 않는지 체크
                answer.remove([x, y, a])
                
    return sorted(answer)

n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))