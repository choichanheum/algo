# 위상 정렬 알고리즘 예제 10-5. 
# 위상 정렬 (Topology Sort) : 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘 (방향 그래프의 모든 노드를 '방향성'에 거스르지 않도록 순서대로 나열하는 것)
#   1. 진입차수(특정한 노드로 '들어오는' 간선의 개수) 가 0인 노드를 큐에 넣는다.
#   2. 큐가 빌 때까지 다음의 과정 반복
#       2-1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
#       2-2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
# 큐가 빌 때까지 큐에서 원소를 계속 꺼내서 처리하는 과정을 반복하는 것인데, 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단 가능
# (큐에서 원소가 V번 추출되기 전에 큐가 비어버리면 사이클 존재)
# 위상정렬의 시간 복잡도는 O(V+E) 이다. 차례대로 모든 노드를 확인하면서 해당 노드에서 출발하는 간선을 차례대로 제거해야하기 때문. 결과적으로 노드와 간선을 모두 확인하므로 O(V+E)

'''
입력값
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4


출력값
1 2 5 3 6 4 7

'''

from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0 for _ in range(v+1)]

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    # 진입차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

print(graph)
print(indegree)

topology_sort()