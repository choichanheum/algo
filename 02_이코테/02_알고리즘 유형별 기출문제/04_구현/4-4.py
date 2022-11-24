# Q10 - 자물쇠와 열쇠
# 자물쇠에는 홈이 파여 있고, 열쇠에는 홈과 돌기 부분이 있다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열린다.
# 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안되며, 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있다.
# key 와 lock 의 원소는 0 또는 1로 이루어져 있다. 0은 홈 부분, 1은 돌기 부분이다.
# 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열 수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성하라.
# https://programmers.co.kr/learn/courses/30/lessons/60059


'''
입력값
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

출력값
true

'''

def check(pan, n):
    for a in range(n):
        for b in range(n):
            if pan[a+n][b+n] != 1:
                return False
    return True

def rotate(key):
    m = len(key)
    new = [[0 for _ in range(m)] for _ in range(m)]

    for i in range(m):
        for j in range(m):
            new[j][m-i-1] = key[i][j]
    
    return new

def solution(key, lock):
    answer = False

    # key의 (m,m) 이 lock의 (0,0) 을 체크하는 경우부터 key의 (0,0) 이 lock의 (n,n)을 체크하는 경우를 모두 돌기 위해 3n x 3n 형태의 판을 생성 (3배 크기로 하는 이유는 인덱스 다루기 편해서임)
    m = len(key)
    n = len(lock)

    pan = [[0 for _ in range(3*n)] for _ in range(3*n)]

    # 자물쇠를 판의 정중앙에 위치
    for i in range(n):
        for j in range(n):
            pan[i+n][j+n] = lock[i][j]

    for _ in range(4): # 90도씩 4번 회전
        key = rotate(key) # key를 90도 회전

        for x in range(n-m+1, 2*n):
            for y in range(n-m+1, 2*n):
                # key 를 판에 더함 (맞춰봄)
                for i in range(m):
                    for j in range(m):
                        pan[x+i][y+j] += key[i][j]

                print()
                for i in range(3*n):
                    for j in range(3*n):
                        print(pan[i][j], end=' ')
                    print()
                print()

                # 정중앙의 자물쇠를 돌면서 key 가 일치하는지 확인 (전부 1이어야함)
                if check(pan, n):
                    answer = True

                    return answer

                # key 를 판에서 뺌
                for i in range(m):
                    for j in range(m):
                        pan[x+i][y+j] -= key[i][j]

    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))