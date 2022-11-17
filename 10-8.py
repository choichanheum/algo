# 그래프 이론 예제 10-8. 커리큘럼 (실전)
# N개의 강의를 듣고자 한다. 모든 강의는 1번부터 N번까지의 번호를 가지고, 선수 강의가 있는 강의는 선수 강의를 들어야만 해당 강의를 들을 수 있다.
# 또한 동시에 여러 개의 강의를 들을 수 있다.
# N개의 강의 정보가 주어져씅ㄹ 때, N개의 강의에 대하여 수강하기까지 걸리는 최소시간을 각각 출력하라.

'''
입력값
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1


출력값
10
20
14
18
17

'''

from collections import deque
import copy

n = int(input())

indegree = [0 for _ in range(n+1)]

graph = [[] for _ in range(n+1)]

time = [0 for _ in range(n+1)]

for i in range(1, n+1):
    lecture = list(map(int, input().split()))
    time[i] = lecture[0]

    for j in lecture[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

def topology_sort():
    # result = time
    result = copy.deepcopy(time) # 바로 위 소스코드는 얕은 복사여서 리스트 조작 시 문제 발생할 수 있음
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()