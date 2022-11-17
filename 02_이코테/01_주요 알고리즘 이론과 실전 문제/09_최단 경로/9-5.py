# 최단 경로 예제 9-5. 전보 (실전)
# 어떤 나라에는 N 개의 도시가 있고, 각 도시는 보내고자 하는 메시지가 있는 경우 다른 도시로 전보를 보내서 해당 메시지를 전달할 수 있다.
# C 라는 도시에서 위급 상황이 발생하여 최대한 많은 도시로 메시지를 보내고자 할 때, C 에서 보낸 메시지를 받게 되는 도시의 총 개수와 모두 받는 데까지 걸리는 시간을 계산하라.

'''
입력값
3 2 1
1 2 4
1 3 2


출력값
2 4


'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수 N, 통로의 개수 M, 메세지를 보내고자하는 도시 C (start) 입력
n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]

distance = [INF for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(graph)
print(distance)

# 도달할 수 있는 노드의 개수
count = 0

# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단거리
max_distance = 0

for d in distance:
    # 도달할 수 있는 노드인 경우 (+시작 노드는 제외)
    if d != INF and d != 0:
        count += 1
        max_distance = max(max_distance, d)

print(count, max_distance)