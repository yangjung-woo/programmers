# 전력망을 둘로 나누되 두 전력망 사이 노드 수가 최대한 일치하도록 나누는 문제 
# 두 송전탑 사이 차이를 answer로 반환 
# 예상대로 dfs 로 풀면 가능하다 


def dfs(now,scan_graph):

    visited[now] = True
    node = 1

    # 모든 연결된 노드들 중에서 방문하지 않은 노드가 있다면 dfs
    for next_node in scan_graph[now]:# 
        if visited[next_node] == False: 
            node+=dfs(next_node,scan_graph)
    return node


def solution(n, wires):

    answer = -1
    graph = [[] for _ in range(n+1)]
    global visited
    visited = [False]*(n+1)
    # 그래프를 생성 
    for w in wires:
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])
    ans_list = []
    for w in wires:

        #scan_graph= graph.copy() # 파이썬 에서 = 리스트는 수정이 원본에도 반영된다 , 따라서 shallow copy해야함 
        
        # 2차원 배열의 경우 깊은 복사를 해야 하기때문에  행 별 원소를 일일이 복사해줘야함 
        scan_graph = [g[:] for g in graph]
        visited = [False]*(n+1)

        # 연결을 제거 
        scan_graph[w[0]].remove(w[1])
        scan_graph[w[1]].remove(w[0])
        # 단절된 점에서 dfs 서치 
        node1 = dfs(w[0],scan_graph)
        node2= n- node1
        gap = abs(node1- node2)
        ans_list.append(gap)

    return (min(ans_list))


print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))