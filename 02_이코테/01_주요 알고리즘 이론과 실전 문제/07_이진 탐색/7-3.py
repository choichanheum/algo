# 빠르게 입력받기 예제 7-3.
# 데이터의 개수가 1,000만 개 넘어가거나 탐색 범위의 크기가 1,000억 이상이면 이진 탐색을 의심
# 이때 input() 함수를 사용하면 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있으므로 sys 라이브러리의 readlin() 함수를 이용하자.
# sys 라이브러리를 사용할 때는 한 줄 입력받고 나서 rstrip() 함수를 꼭 호출해야함
#   -> readline() 으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백문자를 제거하기위함.

'''
입력값
Hello, Coding Test!

출력값
Hello, Coding Test!

'''

import sys

# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

# 입력받는 문자열 그대로 출력
print(input_data)