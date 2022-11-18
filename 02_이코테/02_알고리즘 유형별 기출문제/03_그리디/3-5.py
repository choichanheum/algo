# 그리디 문제 05 - 볼링공 고르기
# A,B 두 사람이 볼링을 친다. 서로 다른 무게의 볼링공을 고르려고 한다. 볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여된다.
# 같은 무게의 공이 여러 개 있을 수 있지만, 서로 다른 공으로 간주한다. 볼링공의 무게는 1~M 까지의 자연수 형태이다.
# N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하라.

'''
입력값
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2

출력값
8

25

'''

# list의 앞에서부터 차례대로 뒷 원소들과의 조합을 뽑는 대신 무게가 서로 다를때만 count 를 증가시킨다.

n, m = map(int, input().split())

data = list(map(int, input().split()))

count = 0

for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        if data[i] != data[j]:
            count += 1
        
print(count)



'''
책의 풀이

n, m = map(int, input().split())

data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0

for i in range(1, m+1):
    n -= array[i] # 무게가 1인 볼링공의 개수 (A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수의 곱하기

print(result)
'''

