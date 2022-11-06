# 재귀 함수 (팩토리얼) 예제 5-5. 
# 재귀 함수를 이용하는 대표적인 예제인 팩토리얼 문제를 2가지 방식으로 구현한 것(반복적, 재귀적)
# 소스 코드를 반복적으로 구현한다는 말은 반복문을 이용한다는 의미이며, 재귀적으로 구현한다는 말과 대비되는 의미로 사용됨
# 재귀적으로 구현한 소스코드가 더 간결한 것을 알 수 있는데, 이유는 재귀 함수가 수학의 점화식(재귀식)을 그대로 코드로 옮겼기 때문이다. (다이나믹 프로그래밍 dp 로 이어지므로 중요한 개념임)

'''
입력값


출력값

'''

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1 부터 n 까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1

    # n! = n * (n-1)! 을 그대로 코드로 작성 
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력 (n = 5)
print('반복적으로 구현', factorial_iterative(5))
print('재귀적으로 구현', factorial_recursive(5))