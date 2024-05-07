def solution(keyinput, board):
    answer = []
    bx, by, ax, ay = - (board[0] // 2), - (board[1] // 2),  board[0] // 2, board[1] // 2
    nx, ny = 0, 0
    for key in keyinput:
        if key == "left": # -1, 0
            if bx <= nx - 1 <= ax and by <= ny <= ay:
                nx = nx - 1
                ny = ny
        elif key == "right": # +1, 0
            if bx <= nx + 1 <= ax and by <= ny <= ay:
                nx = nx + 1
                ny = ny
        elif key == "up": # 0, +1
            if bx <= nx <= ax and by <= ny + 1 <= ay:
                nx = nx 
                ny = ny + 1
        elif key == "down":
            if bx <= nx <= ax and by <= ny - 1 <= ay:
                nx = nx
                ny = ny - 1
    return [nx, ny]