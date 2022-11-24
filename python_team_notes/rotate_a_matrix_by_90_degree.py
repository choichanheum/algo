# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산

    result = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        for j in range(m):
            result[j][m-i-1] = a[i][j]

    return result