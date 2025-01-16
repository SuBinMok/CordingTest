import sys
from collections import deque

N = int(sys.stdin.readline())
field = []
for _ in range(N):
    field.append(sys.stdin.readline().strip())
ncb_vis = [[0]*N for _ in range(N)]
cb_vis = [[0]*N for _ in range(N)]

result = []
cb_q =  deque()
ncb_q =  deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ncb_c, cb_c = 0, 0

def bfs_ncb(clr): #not color blindness
    while ncb_q:
        x, y = ncb_q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and field[nx][ny] == clr and ncb_vis[nx][ny] == 0:
                ncb_q.append([nx, ny])
                ncb_vis[nx][ny] = 1

def bfs_cb(clr): # color blindness
    while cb_q:
        x, y = cb_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and cb_vis[nx][ny] == 0:
                if clr == "B":
                    if field[nx][ny] == clr:
                        cb_q.append([nx, ny])
                        cb_vis[nx][ny] = 1
                else:
                    if field[nx][ny] == "G" or field[nx][ny] =="R":
                        cb_q.append([nx, ny])
                        cb_vis[nx][ny] = 1


for i in range(N):
    for j in range(N):
        if ncb_vis[i][j] == 0:
            clr = field[i][j]
            ncb_q.append([i, j])
            bfs_ncb(clr)
            ncb_vis[i][j] = 1
            ncb_c += 1
        if cb_vis[i][j] == 0:
            clr = field[i][j]
            cb_q.append([i, j])
            bfs_cb(clr)
            cb_vis[i][j] = 1
            cb_c += 1
print(ncb_c, cb_c)