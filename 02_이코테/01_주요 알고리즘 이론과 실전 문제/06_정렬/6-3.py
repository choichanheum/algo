# 퀵 정렬 예제 6-3.
# 정렬 알고리즘에서 가장 많이 사용됨. 퀵 정렬과 병합 정렬 알고리즘은 대부분의 프로그래밍 언어에서 정렬 라이브러리의 근간이됨
# 퀵 정렬을 수행하기 전에는 큰 숫자와 작은 숫자를 교환할 때 사용되는 기준인 피벗을 어떻게 설정할 것인지 미리 명시해야함
# 피벗을 설정하고 리스트를 분할하는 방법에 따라서 여러가지 퀵 정렬로 구분되는데, 책에서는 가장 대표적인 방식인 '호어 분할' 방식을 기준으로 설명함
# 호어 분할 방식 : 리스트에서 첫번째 데이터를 피벗으로 정한다.
# 퀵 정렬의 시간복잡도는 O(NlogN) 이다. 앞의 선택 정렬, 삽입 정렬에 비해 매우 빠르다. (단, 최악의 경우 시간복잡도는 O(N²)가 된다.)
# 데이터가 무작위로 입력되는 경우 퀵 정렬이 빠르게 동작할 확률이 높다.

'''
입력값



출력값

'''

array = [5, 7, 9, 0, 3 , 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return

    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[right], array[left] = array[left], array[right]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)



'''
# 파이썬의 장점을 살린 퀵 정렬 소스코드

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x<= pivot] #분할된 왼쪽 부분
    right_side = [x for x in tail if x> pivot] #분할된 왼쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

'''