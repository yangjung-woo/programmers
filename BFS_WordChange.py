from collections import deque
from collections import defaultdict
def nextWord(current, words):

    n = len(current)
    neighbor_node =[]
    for w in words:
        s1 = list(current)
        s2 = list(w)
        diff = 0
        for i in range(n):
            if s1[i] != s2[i]:
                diff +=1
        
        if diff ==1: # 차이가 단 개다 ==> 변환 가능한 단어이다 
            neighbor_node.append(w)
    
    return neighbor_node


             

def bfs(begin , target , words):
    count = 0
    minn = 1e9

    visited = defaultdict(lambda:False)
    # 이웃하는 begin에서 이웃하는 모든 노드들을 큐에 저장 
    queue = deque(nextWord(begin,words)) 

    while(queue): # queue 가 존재하면 반복을 계속 시행 
        size = len(queue)
        count +=1
        for i in range(size):
            key= queue.popleft() # 큐에서 추출후 , 해당 노드 탐색
            visited[key] = True
            # 만약 target이면 종료 + 최단거리 갱신 
            if key == target and count <minn:
                minn = count
            
            # 방문한 key에서 이웃한 모든 노드 또다시 탐색 
            for candidate in nextWord(key,words):
                if visited[candidate] == False: 
                    queue.append(candidate)
    
    if minn == 1e9:
        return 0
    else:
        return minn




def solution(begin, target, words):

    answer =bfs(begin, target, words)
    return answer

print(solution("hit",	"cog"	,["hot", "dot", "dog", "lot", "log", "cog"]) )