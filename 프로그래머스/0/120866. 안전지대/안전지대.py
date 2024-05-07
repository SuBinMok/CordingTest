def solution(board):
    answer = 0
    dy,dx = [-1,0,1,0,-1,1,1,-1],[0,1,0,-1,1,1,-1,-1]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                for k in range(8):
                    if 0 <= i + dx[k] < len(board) and 0 <= j+dy[k] < len(board):
                        if board[i+dx[k]][j+dy[k]] == 0:
                            board[i+dx[k]][j+dy[k]] = 2
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                answer+=1
    return answer