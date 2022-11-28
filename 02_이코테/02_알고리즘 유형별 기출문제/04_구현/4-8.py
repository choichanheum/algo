# Q14 - 외벽 점검
# 동그랗고 둘레가 n미터인 레스토랑의 외벽을 점검하려고 한다. 점검 시간은 1시간으로 제한되고, 내부 공사 도중 외벽의 취약 지점들이 손상되지 않았는지 주기적으로 친구들을 보내 점검해야한다.
# 레스토랑의 정북 방향을 0으로 하고, 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리로 나타낸다. 친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서 이동한다.
# 외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist 가 매개변수로 주어질 때, 취약 지점을 점검하기 위해 보내야 하는
# 친구 수의 최솟값을 return하도록 solution 함수를 완성하라.
# https://programmers.co.kr/learn/courses/30/lessons/60062


'''
입력값
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]

출력값
2

1

'''

from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)

    answer = len(dist)+1 # 투입할 친구 수의 최솟값을 구해야 하므로 친구 수의 +1 로 초기화

    weaks = weak + [w+n for w in weak]

    # print(weaks)

    permu = list(permutations(dist, len(dist)))

    # print(permu)

    for start in range(length): # 취약점(weak)만큼 반복
        for friends in permu: # 친구들(dist)를 순열로 구한 모든 경우의 수만큼 반복
            count = 1 # 투입할 친구 수
            position = weaks[start] + friends[count-1] # 해당 친구가 점검할 수 있는 마지막 위치

            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start+length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weaks[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입할 친구가 없으면 종료
                        break
                    position = weaks[index] + friends[count-1]

            answer = min(answer, count) # 최솟값 계산

    if answer > len(dist):
        return -1

    return answer

n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]

print(solution(n, weak, dist))