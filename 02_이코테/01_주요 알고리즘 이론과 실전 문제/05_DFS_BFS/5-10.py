# DFS/BFS 예제 5-10. 음료수 얼려 먹기 (실전)
# N x M 크기의 얼음 틀이 있다. 구멍이 뚫린 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫린 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결된 것으로 간주한다.
# 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하라.

'''
입력값
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111


출력값
8
'''

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):

    if x<0 or x>=n or y<0 or y>=m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 9
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    else:
        return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

for i in range(n):
    for j in range(m):
        print(graph[i][j], end = ' ')
    print()