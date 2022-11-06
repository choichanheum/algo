# 재귀 함수 예제 5-3. 
# 자기 자신을 다시 호출하는 함수
# 아래 재귀 함수를 실행하면 print를 계속 출력하다가 오류메시지와 함께 멈춤. 파이썬 인터프리터의 호출 횟수 제한을 넘어섰기 때문
# 

'''
입력값


출력값

'''

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()