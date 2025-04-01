def solution(park, routes):
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j
                break
    
    # dir = {"N":(0,-1), "S":(0, 1), "W":(-1,0), "E":(1,0)}   
    dir = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}    
    for r in routes:
        d, m = r.split(" ")
        bx, by = x, y
        for _ in range(int(m)):
            nx = x + dir[d][0]
            ny = y + dir[d][1]
            if 0 <= nx < len(park) and 0 <= ny < len(park[0]) and park[nx][ny] != "X":
                x, y = nx, ny
            else:
                x, y = bx, by
                break
    return x, y