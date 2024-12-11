import sys
from collections import deque
row, col = map(int,sys.stdin.readline().split())
vis = [[0]*col for _ in range(row)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
mirro = [[int(i) for i in sys.stdin.readline().strip()] for _ in range(row)]
ant = 0
que = deque()

def bfs(i, j, a):
    vis[i][j] = a + 1
    que.append([i, j])
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < row and 0 <= ny < col and mirro[nx][ny] == 1 and vis[nx][ny] == 0:
                que.append([nx, ny])
                vis[nx][ny] = vis[x][y] + 1
                a = vis[nx][ny]
    return a


for i in range(row):
    for j in range(col):
        if mirro[i][j] == 1 and vis[i][j] == 0:
            bfs(i, j, ant)

print(vis[row-1][col-1])
