# 이진 탐색 예제 7-4. 부품 찾기 (실전)
# N개의 부품이 있을 때 각 부품은 정수 형태의 고유한 번호가 있다. 손님이 M개 종류를 문의했을 때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성하라.
# 있으면 yes, 없으면 no 출력
# 이진탐색의 시간복잡도 = 부품을 찾는 과정에서 최악의 시간복잡도 O(M x logN) + N개 부품을 정렬하기 위해 요구되는 시간복잡도 O(N x logN) = O((M+N) x logN)

'''
입력값
5
8 3 7 9 2
3
5 7 9

출력값
no yes yes

'''

# 이진 탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# N(가게의 부품 개수) 입력
n = int(input())

# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행

# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())

# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')




# 계수 정렬

# N(가게의 부품 개수)을 입력받기
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in list(map(int, input().split())):
    array[i] = 1

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')




# 집합 자료형 이용

# N(가게의 부품 개수)을 입력받기
n = int(input())

# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())

# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 욫어한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')