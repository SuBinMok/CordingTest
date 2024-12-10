import sys
from collections import deque
row, col = map(int,sys.stdin.readline().split())
vis = [[0]*col for _ in range(row)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
mirro = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
cnt = 0
ant = 0
que = deque()
def bfs(i, j):
    vis[i][j] = 1
    c = 1

    que.append([i, j])
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < row and 0 <= ny < col and mirro[nx][ny] == 1 and vis[nx][ny] == 0:
                que.append([nx, ny])
                vis[nx][ny] = 1
                c += 1
    return c
for i in range(row):
    for j in range(col):
        if mirro[i][j] == 1 and vis[i][j] == 0:
            cnt+=1
            ant = max(bfs(i, j), ant)

print(cnt)
print(ant)
