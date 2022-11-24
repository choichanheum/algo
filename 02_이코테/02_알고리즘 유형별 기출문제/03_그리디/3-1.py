# Q01 - 모험가 길드
# 마을에 모험가 N명이 있다. N명의 모험가를 대상으로 공포도를 측정했는데, 안전을 위해 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여하도록 규정했다.
# N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하라.


'''
입력값
5
2 3 1 2 2

20
1 2 2 3 3 3 4 4 4 5 5 5 5 5 6 6 6 6 6 6

27
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 7 7 7 7 7 7

6
4 3 3 3 3 2

출력값
2

5

6

2

'''

n = int(input())

data = list(map(int, input().split()))

data.sort()

result = 0

while data:
    target = data[-1]
    for _ in range(target):
        if len(data) == 0:
            continue
        data.pop()
    result += 1

print(result)


'''
책의 풀이

n = int(input())

data = list(map(int, input().split()))

data.sort()

count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함한 모험가의 수 초기화

print(result) # 총 그룹의 수 출력

'''