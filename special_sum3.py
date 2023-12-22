def solution(left, right):
    answer = 0
    for i in range(left , right+1): # i 가 거듭제곱 꼴이면 약수의 갯수는 홀수개이고 이외는 짝수개
        if i**0.5 == int(i**0.5):# 거듭제곱 꼴이면 
            answer -= i
        else:
            answer += i
     
    return answer
