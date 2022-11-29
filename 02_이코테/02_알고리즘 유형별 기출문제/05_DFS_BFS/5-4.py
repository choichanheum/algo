# Q18 - 괄호 변환
# '(' 와 ')' 로만 이루어진 문자열이 있을 경우, '(' 의 개수와 ')' 의 개수가 같다면 이를 균형잡힌 괄호 문자열이라고 부른다.
# '('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열이라고 부른다.
# '(' 와 ')' 로만 이루어진 문자열 w가 "균형잡힌 괄호 문자열" 이라면 다음과 같은 과정을 통해 "올바른 괄호 문자열"로 변환할 수 있다.
#    1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
#    2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
#    3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
#      3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
#    4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
#      4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
#      4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
#      4-3. ')'를 다시 붙입니다. 
#      4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
#      4-5. 생성된 문자열을 반환합니다.
# "균형잡힌 괄호 문자열" p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 "올바른 괄호 문자열"로 변환한 결과를 return 하도록 solution 함수를 완성하라.
# https://programmers.co.kr/learn/courses/30/lessons/60058


'''
입력값
"(()())()"

")("

"()))((()"

출력값
"(()())()"

"()"

"()(())()"

'''
def split(p):
    u = ""
    v = ""

    count = 0

    split = len(p)

    for i, x in enumerate(p):
        if x == "(":
            count += 1
        elif x == ")":
            count -= 1

        if count == 0:
            split = i
            break
        
    u = p[:i+1]
    v = p[i+1:]

    return u, v

def check(p):
    count = 0

    for i, x in enumerate(p):
        if x == "(":
            count += 1
        elif x == ")":
            if count == 0: # 짝이 맞는 상태에서 ")"가 또 들어오면 올바르지 않음
                return False
            count -= 1

    return True

def solution(p):
    answer = ''

    if not p:
        return ""
    
    u, v = split(p)
    
    if check(u):
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)
    
    return answer

p = "()))((()"

print(solution(p))