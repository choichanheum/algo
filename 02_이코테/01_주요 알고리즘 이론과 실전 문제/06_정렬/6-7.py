# 정렬 예제 6-7. 성적이 낮은 순서로 학생 출력하기 (실전)
# N명의 학생 정보가 있다. 정보는 이름과 성적으로 구분된다.
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하라.

'''
입력값
2
홍길동 95
이순신 77

출력값
이순신 홍길동
'''

n = int(input())

array = []

for i in range(n):
    name, score = input().split()
    array.append((name, int(score)))

print(array)

array = sorted(array, key=lambda i:i[1])

print(array)

for data in array:
    print(data[0], end=' ')