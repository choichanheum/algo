# Q09 - 문자열 압축
# 문자열을 압축하려고 한다. 문자열 s 가 주어졌을 때 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성하라.
# https://programmers.co.kr/learn/courses/30/lessons/60057


'''
입력값
aabbaccc

ababcdcdababcdcd

abcabcdede

abcabcabcabcdededededede

xababcdcdababcdcd

출력값
7

9

8

14

17

'''

def solution(s):
    answer = int(1e9)

    unit = 1 # 문자열 자를 단위

    while unit<=len(s)//2+1:
        repeat = 1 # 반복 횟수를 저장할 변수
        result = "" # 문자열을 저장할 변수

        for i in range(0, len(s), unit): # 단위만큼씩 건너뛰면서 반복문 수행
            if s[i:i+unit] == s[i+unit:i+unit*2]: # 현재값과 다음값을 비교하여 같으면 반복횟수를 1 증가
                repeat += 1
            else: # 현재값과 다음값을 비교하여 다르면 반복횟수+문자열 반환
                result += str(s[i:i+unit]) if repeat == 1 else str(repeat)+str(s[i:i+unit])
                repeat = 1 # 반복횟수를 1로 초기화

        if len(result) < answer: # 길이가 작은 값으로 덮어씌움
            answer = len(result)

        unit += 1 # 단위 1 증가
        
    return answer

s = input()

solution(s)

print(solution(s))


'''
# 책의 풀이

def solution(s):
    answer = len(s)

    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1

        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면 (더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1

        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer

'''