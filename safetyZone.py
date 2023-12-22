# 다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 
# 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다
# 지뢰 = 1  , 안전지역의 칸 수를 반환 
# nxn board 


def solution(board):
    answer =0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 1: #  x와 y에 다른 분기점 


                if x>0 and y>0 and x<len(board)-1 and y<len(board)-1:
                    if board[y-1][x-1] ==0:
                        board[y-1][x-1] = 2

                    if board[y-1][x] ==0:
                        board[y-1][x] = 2

                    if board[y-1][x+1] == 0:
                        board[y-1][x+1]=2

                    if board[y][x-1] == 0:                        
                        board[y][x-1] = 2

                    if board[y][x+1] == 0:
                        board[y][x+1] = 2

                    if board[y+1][x-1] ==0:
                        board[y+1][x-1] = 2

                    if board[y+1][x] ==0:
                        board[y+1][x] = 2

                    if board[y+1][x+1] ==0:
                        board[y+1][x+1] = 2
                else:

                    if y==0: # 첫번째 행 일 경우
                        if x == 0: # 가장 왼쪽 모서리 
                            if board[y][x+1] ==0:
                                board[y][x+1] = 2
                            if board[y+1][x+1] ==0:
                                board[y+1][x+1] = 2
                            if board[y+1][x] ==0:
                                board[y+1][x] = 2
                        elif x == len(board[x])-1: # 우측 모서리 
                            if board[y][x-1] ==0:
                                board[y][x-1] = 2
                            if board[y+1][x-1] == 0:
                                board[y+1][x-1] = 2
                            if board[y+1][x] ==0:
                                board[y+1][x] = 2
                        else: 
                            if board[y][x-1] ==0:
                                board[y][x-1] = 2

                            if board[y][x+1] ==0:    
                                board[y][x+1] = 2

                            if board[y+1][x] ==0:
                                board[y+1][x] = 2

                            if board[y+1][x-1] ==0:
                                board[y+1][x-1] = 2

                            if board[y][x-1] ==0:
                                board[y][x-1] = 2
                    if y==len(board)-1:
                        if x == 0: # 가장 왼쪽 모서리  
                            if board[y][x+1] ==0:
                                board[y][x+1] = 2
                            if board[y-1][x+1] ==0:
                                board[y-1][x+1] = 2
                            if board[y-1][x] ==0:
                                board[y-1][x] = 2
                        elif x == len(board[x])-1: # 우측 모서리 
                            if board[y][x-1] ==0:
                                board[y][x-1] = 2
                            if board[y-1][x-1] ==0:
                                board[y-1][x-1] = 2
                            if board[y-1][x] ==0:
                                board[y-1][x] = 2
                        else: 
                            if board[y][x-1] ==0:
                                board[y][x-1] = 2
                            if board[y][x+1] ==0:
                                board[y][x+1] = 2
                            if board[y-1][x] ==0:
                                board[y-1][x] = 2
                            if board[y-1][x-1] ==0:
                                board[y-1][x-1] = 2
                            if board[y-1][x+1] ==0:
                                board[y-1][x+1] = 2

                    if x==0: # 첫번째 열 
                        if y<len(board)-1 and y>0:
                            if board[y+1][x] ==0:
                                board[y+1][x] = 2
                            if board[y+1][x+1] ==0:
                                board[y+1][x+1] = 2
                            if board[y][x+1] ==0:
                                board[y][x+1] = 2
                            if board[y-1][x] ==0:
                                board[y-1][x] = 2
                            if board[y-1][x+1] ==0:
                                board[y-1][x+1] = 2
                    if x==len(board)-1:
                        if y<len(board)-1 and y>0:
                            if board[y+1][x-1] ==0:
                                board[y+1][x-1] = 2
                            if board[y+1][x] ==0:
                                board[y+1][x] = 2
                            if board[y][x-1] ==0:
                                board[y][x-1] = 2
                            if board[y-1][x-1] ==0:
                                board[y-1][x-1] = 2
                            if board[y-1][x] ==0:
                                board[y-1][x] = 2
    # for end 
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x]==0:
                answer+=1


    return answer

board = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

print(solution(board))