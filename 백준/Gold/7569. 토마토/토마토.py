import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
field = [[list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)] for _ in range(H)]
vis = [[[0]*M]*N]*H
q = deque()
days = 0
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        h, x, y = q.popleft()
        for i in range(6):
            nh = h + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M:
                if field[nh][nx][ny] == 0:
                    q.append([nh, nx, ny])
                    field[nh][nx][ny] = field[h][x][y] + 1


for h in range(H):
    for i in range(N):
        for j in range(M):
            if field[h][i][j] == 1:
                q.append([h, i, j])
bfs()

not_complete = False
for h in range(H):
    for i in range(N):
        for j in range(M):
            if field[h][i][j] == 0:
                not_complete = True
            days = max(days, field[h][i][j])
if not_complete:
    print(-1)
else:
    print(days-1)