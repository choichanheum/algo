# 그리디 문제 03 - 문자열 뒤집기
# 0과 1로만 이루어진 문자열 S를 가지고 있다. 이 문자열 S에 있는 모든 숫자를 전부 같게 만드려고 한다.
# 할 수 있는 작업은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
# S가 주어졌을 때, 작업의 최소 횟수를 출력하라.

'''
입력값
0001100


출력값
1

'''

# 처음부터 돌면서 다음숫자가 달라지는 횟수를 기록

s = list(map(int, input()))

count = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1

print((count+1)//2)



'''
책의 풀이

s = list(map(int, input()))

count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

if s[0] == 1:
    count0 += 1
else:
    count1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == 1:
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

'''