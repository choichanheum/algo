# 정렬 예제 6-8. 두 배열의 원소 교체 (실전)
# 두 개의 배열 A, B 가 있다. 두 배열은 각각 N 개의 원소로 이루어져 있다.
# 최대 K 번의 바꿔치기 연산을 수행할 수 있는데, 배열A의 모든 원소의 합이 최대가 되도록하는 것이 최종 목표이다.
# N, K, 배열 A 와 B 의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 구하라.

'''
입력값
5 3
1 2 5 4 3
5 5 6 6 5

출력값
26
'''

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)

print(a)
print(b)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(a)
print(b)

print(sum(a))