# Q08 - 문자열 재정렬
# 알파벳 대문자와 숫자(0~9)로만 이루어진 문자열이 입력으로 주어진다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력하라.


'''
입력값
K1KA5CB7

AJKDLSI412K4JSJ9D

출력값
ABCKK13

ADDIJJJKKLSS20

'''

text = input()

digit = []
alpha = []

for i in range(len(text)):
    if text[i].isdigit():
        digit.append(int(text[i]))
    else:
        alpha.append(text[i])

alpha.sort()

print(''.join(alpha)+str(sum(digit)))