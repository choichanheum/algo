# Q06 - 무지의 먹방 라이브
# 프로그래머스 링크 통해서 풀어야 하는 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42891

'''
입력값
food_time = [3, 1, 2]
k = 5

출력값
result = 1

'''

# 효율성까지 고려한 풀이 (해설)
import heapq

def solution(food_times, k):

    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 더이상 먹을 음식이 없는 것이므로 -1을 반환
    if k >= sum(food_times):
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐를 이용   *음식번호는 인덱스+1
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    
    length = len(food_times) # 남은 음식의 개수

    # sum_value + ((현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수) 와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x: x[1]) # 음식의 번호 기준으로 정렬
    
    return result[(k - sum_value) % length][1]

food_times = [2, 5, 7]
k = 8

print(solution(food_times, k))

'''
내 풀이 : 단순하게 1씩 증가시키면서 조건에 맞는 동작 수행 (정확성은 통과하지만 효율성 통과못함)

def solution(food_times, k):
    answer = 0
    count = 0

    while k >= count:
        answer %= len(food_times)

        if len(food_times) == food_times.count(0):
            return -1

        if food_times[answer] > 0:
            food_times[answer] -= 1
            answer += 1
            count += 1
        else:
            answer += 1
 
    return answer

food_times = [2, 5, 7]
k = 8

print(solution(food_times, k))
'''