# 하노이는 그냥 암기   
#         hanoi(start,end,inter,n-1,answer) # end <-> inter , n-1
#        hanoi(start,inter,end,1,answer) # 그대로 n=1
#        hanoi(inter,start,end,n-1,answer) # inter <-> start  n-1
def hanoi(start,inter,end,n,answer):
    
    if n==1:
        answer.append([start,end])
    else: 
        hanoi(start,end,inter,n-1,answer) # end <-> inter , n-1
        hanoi(start,inter,end,1,answer) # 그대로 n=1
        hanoi(inter,start,end,n-1,answer) # inter <-> start  n-1
    return 

def solution(n):
    answer=[]
    hanoi(1,2,3,n ,answer)
    return answer

print(solution(4))