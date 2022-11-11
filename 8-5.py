# 다이나믹 프로그래밍 예제 8-5. 효율적인 화폐 구성 (실전)
# N 가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
# 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
# 불가능할때는 -1 을 출력한다.

'''
입력값
2 15
2
3

3 4
3
5
7

출력값
5

-1

'''

n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)

d[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-array[i]]+1)

# 계산된 결과 출력
if d[m] == 10001: #최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])


print(d)