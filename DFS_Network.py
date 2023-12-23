# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다
# 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다
# 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

def dfs(n,computers,now,visit):
    visit[now] = True
    for connect in range(n):
        if connect != now and computers[now][connect] ==1 and visit[connect] ==False : 
            dfs(n,computers,connect,visit )



def solution(n, computers):

    visit = [ False for _ in range(n)]
    answer = 0
    for i in range(n):
        if visit[i] == False:
            dfs(n,computers , i , visit)  # 탐색시 모든 노드를 DFS 탐색
            answer+=1
    return answer


print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))