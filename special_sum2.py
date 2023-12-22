def solution(left, right):
    answer = 0
    for i in range(left , right+1):
        count=0
        for j in range(1,i+1): # 약수의 갯수 판별 
            if i % j ==0:
                count+=1
        
        if count %2 ==0: # 약수가 짝수개 이면 더하기 
            answer += i
        else: # 홀수개이면 빼기 
            answer -=i


    return answer
