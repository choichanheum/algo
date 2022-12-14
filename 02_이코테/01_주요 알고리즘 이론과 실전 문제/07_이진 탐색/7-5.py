# 이진 탐색 예제 7-5. 떡볶이 떡 만들기 (실전)
# 떡볶이 떡을 만들어야하는데 떡의 길이는 일정하지 않고, 대신에 한 봉지에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
# 절단기에 높이 (H) 를 지정하면 줄지어진 떡을 한번에 절단한다. H 보다 긴떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
# 절단기로 떡을 잘랐을때 손님은 잘린 떡을 가져간다.
# 손님이 요청한 총 길이가 M 일때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하라.

'''
입력값
4 6
19 15 10 17

출력값
15

'''

# 떡의 개수(N) 와 요청한 떡의 길이(M)을 입력받기
n, m = list(map(int, input().split()))

# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점 과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid

    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        start = mid + 1
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 에 기록

    
# 정답 출력
print(result)