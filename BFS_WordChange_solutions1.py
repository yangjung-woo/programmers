# 해당 문제는 최단 거리를 구하는 문제이기에 BFS 가 더 유리하다 

#1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
#2. words에 있는 단어로만 변환할 수 있습니다.

# 가장 짧은 최단 거리를 구하는 것이기 때문에 answer =1000
# 단어가 하나만 다르면 연결되어있음 
from collections import deque
from collections import defaultdict
def nextWord(cur, words):
    ret = []
    for word in words:
        cnt = 0
        for idx in range(len(word)):
            if word[idx] == cur[idx]:
                cnt += 1
        if cnt == len(cur)-1:
            ret.append(word)
    return ret

def bfs(begin, target  , words ):
    count =0
    visited = defaultdict(lambda: False) # default false인 딕셔너리 생성 , 기존에 없던 key를 생성하면
    # 자동으로 False로 초기화 
    queue = deque(nextWord(begin,words)) # words내 begin과 이웃한 모든 노드를 큐에 저장
    minn = 1e9

    while (queue):
        size = len(queue)
        count +=1
        for _ in range(size):
            key = queue.popleft()
            visited[key] = True
            
            if (key == target and count <minn):
                minn = count

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