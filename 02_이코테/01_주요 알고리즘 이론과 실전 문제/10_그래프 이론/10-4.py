# 크루스칼 알고리즘 예제 10-4. 
# 신장 트리 : 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 크루스칼(Kruskal) 알고리즘 : 대표적인 최소 신장 트리 알고리즘(신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘)
#   1. 모든 간선 데이터를 비용에 따라 오름차순 정렬
#   2. 간선을 하나씩 확인하며 현재 간선이 사이클을 발생시키는지 확인
#   3. 발생하지 않는 경우 최소 신장 트리에 포함
# 최소 신장 트리는 일종의 트리 자료구조이므로, 최종적으로 신장 트리에 포함되는 간선의 개수는 '노드의 개수-1' 과 같다.
# 시간복잡도는 간선의 개수가 E개 일때, O(ElogE)이다. 왜냐하면 간선을 정렬하는 작업이 시간이 가장 오래 걸리고, E개의 데이터를 정렬할 때의 시간복잡도가 O(ElogE) 이기 때문

'''
입력값
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25


출력값
159

'''

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0 for _ in range(v+1)] # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a,b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(parent)
print(result)