# 플로이드 워셜 알고리즘 예제 9-3. 
# 플로이드 워셜 (Floyd-Warshall) 알고리즘은 '모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우' 에 사용할 수 있는 알고리즘이다.
# 소스코드가 짧아 구현은 쉬우나, 핵심 아이디어를 이해하는 것이 중요하다.
# 단계마다 O(N²)의 연산을 통해 '현재 노드를 거쳐가는' 모든 경로를 고려한다. 따라서 총 시간 복잡도는 O(N³) 이다.
# 모든 노드에 대하여 다른 모든 노드로가는 최단 거리 정보를 담아야 하기 때문에 2차원 리스트에 '최단 거리' 정보를 저장한다.

'''
입력값
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2


출력값
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0

'''

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A 에서 B 로 가는 비용은 C 라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

# 수행된 결과를 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[i][j] == INF:
            print("INFINITY")
        else:
            print(graph[i][j], end=' ')
    print()
