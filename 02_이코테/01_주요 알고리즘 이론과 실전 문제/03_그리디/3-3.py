# 그리디 예제 3-3. 숫자 카드 게임
# N X M 형태의 카드가 놓여있고, 게임의 룰을 지키며 가장 높은 숫자가 쓰인 카드 한 장을 뽑아야한다.
# 한마디로 각 행마다 가장 작은 수를 찾고, 그 작은 수들 중에서 가장 큰 수를 뽑으면된다.

'''
입력값
3 3
3 1 2
4 1 4
2 2 2

출력값
2
'''
n, m = map(int, input().split())

card = [list(map(int, input().split())) for _ in range(n)]

print(card)

for i in range(n):
    for j in range(m):
        print(card[i][j], end=' ')
    print()

min_cards = []

for i in range(n):
    min_cards.append(min(card[i]))

print(max(min_cards))