# 구현 예제 4-2. 시각
# 정수 N 을 입력하면 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하라
# 하루는 86,400초로 단순히 1씩 증가시키면서 완전 탐색을 수행해도 경우의 수가 100,000을 넘지 않으므로 시간 제한 2초안에 문제 해결이 가능하다.
# 일반적으로 알고리즘 문제를 풀 때는 확인(탐색) 해야할 전체 데이터의 개수가 100만 개 이하일 때 완전 탐색을 사용하면된다.

'''
입력값
5

출력값
11475
'''

n = int(input())

count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)