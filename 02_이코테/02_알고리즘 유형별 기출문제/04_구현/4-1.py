# Q07 - 럭키 스트레이트
# 게임 캐릭터가 필살기 럭키 스트레이트를 사용하려고 한다. 럭키 스트레이트는 특정 조건을 만족할때만 사용가능하다.
# 특정 조건 : 현재 캐릭터의 점수를 N 이라고 할 때, 자릿수를 기준으로 반 나눠서 왼쪽과 오른쪽의 각 자릿수의 합을 더한 값이 서로 동일할 때
# 점수 N 이 주어졌을 때 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하라. (사용가능 : LUCKY , 사용불가 : READY)
# https://www.acmicpc.net/problem/18406


'''
입력값
123402

출력값
7755

'''

n = list(map(int, input()))

half = int(len(n)/2)

left = n[:half]
right = n[half:]

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")