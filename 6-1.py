# 선택 정렬 예제 6-1.
# 가장 작은 데이터를 앞으로 보내는 과정을 N-1 번 반복하면 정렬이 완료됨
# 선택 정렬의 시간복잡도는 O(N²) 이며, N=10000 개 이상이면 급격히 성능이 저하된다.

'''
입력값



출력값

'''

array = [7, 5, 9, 0, 3 , 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)