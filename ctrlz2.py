
def solution(s): # 스택을 사용하는 방법 
    stack = []
    for a in s.split():
        if a != 'Z':
            stack.append(int(a))
        else:
            if stack:
                stack.pop()

    return sum(stack)
