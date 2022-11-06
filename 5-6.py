# 인접 행렬(Adjacency Matrix) 방식 예제 5-6. 

'''
입력값


출력값

'''

INF = 999999999 # 무한의 비용 선언 (infinity)

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7 , 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)