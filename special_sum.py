# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 
# 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

# 소수를 사용한 접근 하지만 틀림 
def isprime(N):
    for i in range(2, int(N**0.5)+1):
        if N % i==0:
            return False
    return True


def solution(left, right):
    answer = 0
    for i in range(left , right+1):
        if isprime(i):
            answer+= i
        else:
            if i**0.5 == int(i**0.5):
                answer -= i
            else:
                answer+=i
    
    return answer

left = 13
right = 17

print(solution(left,right))
    