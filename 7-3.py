# 이진 탐색 예제 7-2.
# 이진 탐색 (Binary Search)은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있음.
# 위치를 나타내는 변수 3개 사용 (탐색하고자 하는 범위의 시작점, 끝점, 중간점)
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교
# 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다는 점에서 시간 복잡도가 O(logN)이다.
# 처리해야할 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 이진 탐색과 같이 O(logN) 의 속도를 내야 하는 알고리즘을 떠올려야 문제를 풀 수 있다.

'''
입력값
10 7
1 3 5 7 9 11 13 15 17 19

10 7
1 3 5 6 9 11 13 15 17 19

출력값
4

원소가 존재하지 않습니다.

'''

# 재귀 함수로 구현한 이진 탐색 소스코드

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start+end)//2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)

    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

# n(원소의 개수) 과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))

# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)



# 반복문으로 구현한 이진 탐색 소스코드

def binary_search2(array, target, start, end):
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

# n(원소의 개수) 과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))

# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search2(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
