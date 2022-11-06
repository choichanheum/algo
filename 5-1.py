# 스택 예제 5-1. 
# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
# 파이썬은 기본 리스트에서 append(), pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작하므로 별도의 라이브러리를 사용할 필요가 없다.

'''
입력값


출력값

'''

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1])
print(stack[::1])
print(stack[::])

stack.reverse()
print(stack)