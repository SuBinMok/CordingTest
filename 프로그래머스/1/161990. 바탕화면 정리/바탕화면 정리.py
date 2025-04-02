from collections import deque
def solution(wallpaper):
    answer = []
    length = 0
    que = []
    h, w = len(wallpaper), len(wallpaper[0])
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j] == "#":
                que.append([i, j])
    min_x, min_y, max_x, max_y = 99999, 99999, 0, 0
    if len(que) > 1:
        for x, y in que:
            
            if min_x >= x:
                min_x = x
            elif max_x < x:
                max_x = x
            if min_y >= y:
                min_y = y
            elif max_y < y:
                max_y = y
        
    else:
        min_x = que[0][0]
        min_y = que[0][1]
        max_x = que[0][0]
        max_y = que[0][1]
            
    return [min_x, min_y, max_x + 1, max_y + 1]
    
