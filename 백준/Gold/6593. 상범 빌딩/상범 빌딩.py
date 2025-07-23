import sys
from collections import deque


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

count = 0

def bfs():
    que = deque([[sz, sy, sx]])

    while que:
        z, y, x = que.popleft()
        if z == ez and x == ex  and y == ey:
            return 'Escaped in {0} minute(s).'.format(visited[z][y][x])
        field[z][y][x] = 1 # 방문
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0 <= nz < L and 0 <= ny < m and 0 <= nx < n and visited[nz][ny][nx] == 0 :
                if field[nz][ny][nx] == '.' or field[nz][ny][nx] == 'E':
                    que.append([nz, ny, nx])
                    visited[nz][ny][nx] = visited[z][y][x] + 1
    return "Trapped!"
while True:
    L, m, n = map(int, sys.stdin.readline().split())
    if L == 0 and m == 0 and n == 0:
        break
    field = [[]*m for _ in range(L)]
    visited = [[[0]*n for _ in range(m)] for _ in range(L)]
    for i in range(L):
        for _ in range(m):
            field[i].append(list(map(str, sys.stdin.readline().strip())))
        sys.stdin.readline()

    for z in range(L):
        for i in range(m):
            for j in range(n):
                if field[z][i][j] == 'S': # start point
                    sx = j
                    sy = i
                    sz = z
                elif field[z][i][j] == 'E': #escape point
                    ex = j
                    ey = i
                    ez = z
    print(bfs())

