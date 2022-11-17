# 그래프 이론 예제 10-6. 팀 결성 (실전)
# 학교에서 학생들에게 0번부터 N번까지의 번호를 부여함. 처음에는 모든 학생이 서로 다른 팀으로 구분되어 총 N+1 개의 팀으로 존재함.
# 선생님이 '팀 합치기' 연산과 '같은 팀 여부 확인' 연산을 사용할 수 있는데, 선생님이 M개의 연산을 수행할 수 있을 때 '같은 팀 여부 확인' 연산에 대한 연산 결과를 출력하라.
# 팀 합치기 연산 : 0 a b 형태 (a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다)
# 같은 팀 여부 확인 연산 : 1 a b 형태 (a번 학생과 b번 학생이 같은 팀에 속해 있는지 확인)

'''
입력값
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1


출력값
NO
NO
YES

'''

# 팀 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 같은 팀 여부 확인
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 입력
n, m = map(int, input().split())
parent = [0 for _ in range(n+1)] 

# 부모테이블의 부모를 자기자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# 연산 판단하여 수행
for i in range(m):
    calc, a, b = map(int, input().split())

    if calc == 0:
        union_parent(parent, a, b)
    elif calc == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
