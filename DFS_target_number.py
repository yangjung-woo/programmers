# 이진 트리를 생각하면 간단하게 DFS를 구현할 수 잇음 

# dfs 구조 1. max_depth 일때 탈출 , 왼쪽노드 탐색 , 오른쪽 노드 탐색  
answer = 0
def dfs( current,target,level ,max_len , numbers) :
    global answer

    if level==max_len:# 종단 노드 도착 

        if current == target:
            answer +=1
            return
        else:
            return
        
    else:
        operand = numbers[level]
        dfs(current+operand ,target , level+1 , max_len, numbers )
        dfs(current-operand ,target , level+1 , max_len , numbers )



def solution(numbers, target):

    dfs(0, target , 0,len(numbers),numbers)
    return answer

numbers =[1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))
