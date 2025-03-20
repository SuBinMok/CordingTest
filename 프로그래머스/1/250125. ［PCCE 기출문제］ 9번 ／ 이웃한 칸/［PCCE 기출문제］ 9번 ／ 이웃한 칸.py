def solution(board, h, w):
    answer = 0
    dx = [-1, 1, 0, 0] #상하좌우
    dy = [0, 0, -1, 1]
    clr = board[h][w]
    for i in range(4):
        if 0<= h+dx[i] < len(board) and 0<= w+dy[i] < len(board[0]):
            if board[h+dx[i]][w+dy[i]] == clr:
                answer+=1
    return answer