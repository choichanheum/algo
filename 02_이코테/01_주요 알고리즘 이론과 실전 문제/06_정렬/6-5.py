# 파이썬의 정렬 라이브러리 예제 6-5.
# 파이썬의 기본 정렬 라이브러리인 sorted() 함수. 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들었는데,
# 일반적으로 퀵 정렬보다 느리지만 최악의 경우에도 시간 복잡도 O(NlogN)을 보장한다는 특징이 있다.
# sorted()함수는 리스트나 딕셔너리 자료형 등을 입력받아서 정렬된 결과를 출력함 (집합 자료형이나 딕셔너리 자료형을 입력받아도 반환되는 결과는 리스트 자료형이다.)
# sorted() 나 sort() 함수를 이용할 때에는 key 매개변수를 입력으로 받을 수 있다. key 값으로는 하나의 함수가 들어가야 하며 이는 정렬 기준이 된다.
# 코딩 테스트에서 정렬 알고리즘이 사용되는 경우
#   1. 정렬 라이브러리로 풀 수 있는 문제 : 단순히 정렬 기법을 알고 있는지 확인. 기본 정렬 라이브러리의 사용법 숙지
#   2. 정렬 알고리즘 원리에 대해서 물어보는 문제 : 선택, 삽입, 퀵 정렬 등의 원리를 알고 있어야 함
#   3. 더 빠른 정렬이 필요한 문제 : 퀵 정렬 기반의 정렬 기법으로는 풀 수 없으며 계수 정렬 등의 다른 알고리즘을 이용하거나 문제에서 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 함

'''
입력값



출력값

'''

# 1. py sorted()
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)

print(result)

# 2. py sort()
# 리스트 변수가 하나 있을 때 내부 원소를 바로 정렬 (리스트 객체의 내장 함수)
# 별도의 정렬된 리스트가 반환되지 않고 내부 원소가 바로 정렬된다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()

print(array)

# 3. py 정렬 라이브러리에서 key를 활용
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

result2 = sorted(array, key=lambda i : i[1]) # 람다 함수 사용
print(result2)