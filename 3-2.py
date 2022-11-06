# 그리디 예제 3-2. 큰 수의 법칙
# 배열의 크기 N, 숫자가 더해지는 횟수 M, 연속으로 더해지는 횟수 초과 불가 K

'''
입력값
5 8 3
2 4 5 4 6

출력값
46
'''

'''
M 이 작아서 간단하게 푸는 풀이법, M이 커지면 시간초과 판정을 받는다.

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

while 1:

    for _ in range(k):

        if m == 0:
            break

        result += first
        m -= 1

    if m == 0:
        break

    result += second
    m -= 1

print(result)
'''


n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

count = ((m // (k+1)) * k) + (m % (k+1))

result = (first*count)+(second*(m-count))

print(result)