# 그리디 문제 06 - 무지의 먹방 라이브
# 프로그래머스 링크 통해서 풀어야 하는 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42891

'''
입력값
food_time = [3, 1, 2]
k = 5

출력값
result = 1

'''

def solution(food_times, k):
    answer = 0

    while k>0:

        if food_times[answer] == 0:
            answer += 1
            continue
        else:
            food_times[answer] -= 1

        answer += 1
        
        if answer == len(food_times):
            answer = 0

        k -= 1

    if food_times[answer] == 0 and food_times[answer+1] == 0:
        return -1

    if food_times[answer] == 0:
        answer += 1

    answer += 1

    return answer

food_times = [2, 5, 7]
k = 8