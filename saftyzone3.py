def solution(board):
    dy= [-1,-1,-1, 0 ,0, 1, 1, 1 ]
    dx =[-1, 0, 1,-1 ,1,-1, 0, 1 ] # 8가지 방향 
    boom_place =[]
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 1:
                boom_place.append((y,x)) # 폭탄 위치 기록

    for y,x in boom_place:
        for i in range(8):
            nx = x +dx[i]
            ny = y +dy[i]
            if 0<=nx<len(board) and 0<=ny<len(board):
                board[ny][nx] = 1

    answer = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 0:
                answer +=1


    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]

print(solution(board))