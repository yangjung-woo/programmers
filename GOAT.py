# 명예의 전당 문제 
# 상위 k 번째 이내면 명예의 전당에 등록 

# k, 1일부터 마지막 날까지 출연한 가수들의 점수인 score가 주어졌을 때,
# 매일 발표된 명예의 전당의 최하위 점수를 return
#k	     score	                        result
# 3	[10, 100, 20, 150, 1, 100, 200]	[10, 10, 10, 20, 20, 100, 100]

def solution(k, score):
    answer = []
    stack =[]
    for i in range(len(score)): 
        if len(stack)<k: # 
            stack.append(score[i])
        else:  # 스택이 꽉 차있으면 
            if score[i] > min(stack):

                stack.pop(stack.index(min(stack))) # 최소값을 방출 
                # pop은 index값을 받아야 한다 
                # 값 그 자체를 지우고 싶다면 .remove 사용 
                stack.append(score[i])
        
        answer.append(min(stack))
    return answer

k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k,score))