import sys
from collections import deque


def bfs(h):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
            if vis[nx][ny] == 0 and arr[nx][ny] > h :
                q.append([nx, ny])
                vis[nx][ny] = 1


k = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

r, c = len(arr), k
q = deque()
ans = []
H = list(set([arr[i][j] for i in range(r) for j in range(c)]))
o = 1
for h in H:
    cnt = 0
    vis = [[0 for _ in range(len(arr))] for _ in range(k)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] > h and vis[i][j] == 0:
                q.append([i, j])
                vis[i][j] = 1
                bfs(h)
                cnt+=1
    ans.append(cnt)
if max(ans) == 0:
    print(1)
else:
    print(max(ans))
