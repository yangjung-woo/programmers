# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다
# 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다
# 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
from collections import deque 
def bfs(n,computers , now , visit):

    visit[now] = True
    queue = deque() # 방문한 노드에서 이웃한 노드들을 저장할 deque
    queue.append(now)
    while(len(queue) !=0 ):
        now = queue.popleft()
        visit[now] = True
        for nexts in range(n):
            if now!= nexts and computers[now][nexts] == 1 and visit[nexts]==False:
                queue.append(nexts)

        


def solution(n, computers):

    visit = [ False for _ in range(n)]
    answer = 0
    queue = deque([]) 
    
    for i in range(n):
        if visit[i] == False:
            bfs(n,computers , i , visit)  # 탐색시 모든 노드를 DFS 탐색
            answer+=1
    return answer


print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))