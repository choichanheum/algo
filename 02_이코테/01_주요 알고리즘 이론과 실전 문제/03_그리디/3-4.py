# 그리디 예제 3-4. 1이 될 때까지
# 어떠한 수 N 이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 수행한다.
# 1. N에서 1뺴기    2. N 을 K로 나누기 (단, N 이 K로 나누어떨어져야함)
# 결과적으로 N 이 1이 될 때까지 1번 혹은 2번 과정을 수행해야하는 최소 횟수를 구하는 프로그램 작성

'''
입력값
25 5

출력값
2
'''
n, k = map(int, input().split())

print(n, k)

count = 0

while n!=1:
    if n%k==0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)



'''
숫자가 매우클때 시간복잡도를 줄이기위한 코드

# N, K공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

'''