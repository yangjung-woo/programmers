# 부서별로 신청한 금액이 들어있는 배열 d와 예산
# budget이 매개변수로 주어질 때, 최대 몇 개의
# 부서에 물품을 지원할 수 있는지 return 하도록 
#solution 함수를 완성해주세요.
# DFS 문제인거같음 
#d	         budget	result
#[1,3,2,5,4]	9	3
#[2,2,3,3]	    10	4
def solution(d, budget):
    answer = 0

    d.sort()
    
    for i in d:
        if budget >= i:
            budget = budget - i
            answer += 1 

    return answer


d =[5,3,4,2,1]
budget = 10

print(solution(d,budget))