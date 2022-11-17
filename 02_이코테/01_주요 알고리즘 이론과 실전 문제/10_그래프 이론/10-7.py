# 그래프 이론 예제 10-7. 도시 분할 계획 (실전)
# 마을은 N개의 집과 M개의 길로 이루어져 있다. 길은 길마다 유지하는데 드는 유지비가 있다.
# 마을이 너무 커서 마을을 2개로 분리하려고 한다. 각 분리된 마을 안의 집들은 모두 서로 연결되어야 한다.
# 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다.
# 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하도록 작업했을 때의 유지비 최소합을 구하라.

'''
입력값
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4


출력값
8

'''

# 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 부모 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 입력 받기
n, m = map(int, input().split())

parent = [0 for _ in range(n+1)]

for i in range(1, n+1):
    parent[i] = i

edges = []
result = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

last = 0 # 최소 신장 트리에 포함되는 간선중에서 가장 비용이 큰 간선

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

# print(edges)
print(result-last)