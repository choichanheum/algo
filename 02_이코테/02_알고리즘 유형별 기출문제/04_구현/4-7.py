# Q13 - 치킨 배달
# 크기가 N x N 인 도시가 있다. 도시의 각 칸은 빈칸, 집, 치킨집 중 하나이다. 도시의 칸은 (r,c)와 같은 형태로 나타내고 1부터 시작한다.
# 집과 가장 가까운 치킨집 사이의 거리를 '치킨 거리' 라고 한다. 각각의 집은 '치킨 거리' 를 가지고 있고, '도시의 치킨 거리' 는 모든 집의 '치킨 거리' 의 합이다.
# (r1, c1) 과 (r2, c2) 사이의 거리는 ｜r1-r2｜+｜c1-c2｜ 로 구한다.
# 도시에 있는 집의 치킨집 중에서 최대 M 개를 고르고, 나머지 치킨집은 모두 폐업시켜야 하는데 '도시의 치킨 거리' 가 가장 작게 해야한다.
# N과 M이 주어졌을 때의 '도시의 치킨 거리' 최소값을 출력하라.
# https://www.acmicpc.net/problem/15686


'''
입력값
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2


출력값
5

'''

# 처음에 생각한 아이디어 : 전체 치킨집을 대상으로 치킨집 별 도시의 치킨 거리를 구해서 최대힙에 넣고, (치킨집 개수-m)만큼 힙에서 pop을 수행하여 치킨집에서 제외함 남은 치킨집으로 도시의 치킨 거리를 계산하여 출력
# 위 아이디어로 풀었는데 결과값이 잘못되어서 결국 combinations 라이브러리 사용하여 풀었음

from itertools import combinations

n, m = map(int, input().split())

city = [[0 for _ in range(n)] for _ in range(n)]

homes = []
chickens = []

# 집과 치킨집의 좌표를 리스트에 추가
for i in range(n):
    city[i] = list(map(int, input().split()))
    for j in range(n):
        if city[i][j] == 1:
            homes.append((i,j))
        elif city[i][j] == 2:
            chickens.append((i,j))

# 전체 치킨집 중 m개를 뽑아서 만들 수 있는 조합
combi_chickens = list(combinations(chickens, m))


# 도시의 치킨 거리 구하기
result = int(1e9)
sum_distance = 0
for chickens in combi_chickens: # 조합의 수 만큼 반복
    for i in range(len(homes)):
        distance = int(1e9)
        r1, c1 = homes[i]
        for j in range(len(chickens)):
            r2, c2 = chickens[j]
            distance = min(distance, abs(r1-r2)+abs(c1-c2))
        sum_distance += distance
    result = min(result, sum_distance)
    sum_distance = 0

print(result)