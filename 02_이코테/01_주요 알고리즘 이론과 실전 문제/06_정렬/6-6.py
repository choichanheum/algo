# 정렬 예제 6-6. 위에서 아래로 (실전)
# 수열을 내림차순으로 정렬하는 프로그램을 만드시오.

'''
입력값
3
15
27
12


출력값
27 15 12
'''

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

# array.sort(reverse=True)
array = sorted(array, reverse=True)

for i in array:
    print(i, end = ' ')