#이 문제는 최단 경로를 찾는 문제로 BFS와 DFS 중 BFS가 더 유리하다.
# 그 이유는 DFS는 모든 경로를 탐색한 후 거리를 비교해야하는 반면 BFS는 탐색 도중 타겟이 발견되면 바로 종료할 수 있기 때문이다.

from collections import deque # 방문 기록을 저장하기 위한 큐가 필요하다 

def solution(maps):

    n, m = len(maps), len(maps[0])
    visits = [[False for _ in range(m)] for _ in range(n)]#  NxN 크기 방문 기록을 저장할 맵 생성
    return bfss(maps,0,0,visits) # 최단거리를 반환 

def bfss(maps,x,y,visits):
    n, m = len(maps), len(maps[0])
    queue = deque([(x , y)]) 
    # 현재 위치 방문함으로 표기 
    visits[x][y] = True
    distance = {(x,y):0}
    dy = [1,0,-1,0]  # dy[i]    i=0 1 2 3 -> 북 동 남 서  
    dx = [0,1,0,-1]
    while queue:
        x , y  = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visits[nx][ny] and maps[nx][ny]:
                # nx , ny 가 맵 범위 안에 있고 , 방문 기록이 없는 노드이고 , 이동가능할때 
                if (nx, ny) == (n-1, m-1):   
                    return distance[(x, y)] + 2  # 최종 도착시 종료
            # 최종 도착 노드가 아니라면 
                queue.append((nx, ny)) 
                distance[(nx, ny)] = distance[(x, y)] + 1
                visits[nx][ny] = True
    return -1
# bfs end 
    
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]  # 0이면 방문 불가 , 1이면 방문 가능 
# maps[4][4] 에 도착하는 방법 

print(solution(maps))