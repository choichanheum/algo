# 최단 경로 예제 9-4. 미래 도시 (실전)
# 방문 판매원 A 가 K번 회사에서 소개팅 후 X번 회사에 도착하려고 할 때의 최소 이동 시간을 구하라.
# 서로 연결된 회사는 양방향으로 이동할 수 있고, 1만큼의 시간이 소요된다.
# X번 회사에 도달할 수 없다면 -1을 출력

'''
입력값
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4

출력값
3

-1

'''

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)

# for i in range(1, n+1):
#     for j in range(1, n+1):
#             print(graph[i][j], end=' ')
#     print()
