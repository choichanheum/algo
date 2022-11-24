# Q04 - 만들 수 없는 금액
# N개의 동전을 가지고 있다. N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하라.

'''
입력값
5
3 2 1 1 9

출력값
8

'''

n = int(input())
coins = list(map(int, input().split()))

coins.sort()

result = 1


for coin in coins:
    if coin > result:
        break
    result += coin

print(result)