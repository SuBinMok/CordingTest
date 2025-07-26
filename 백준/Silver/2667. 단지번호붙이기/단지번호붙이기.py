import sys
from collections import deque


def bfs(n):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
            if vis[nx][ny] == 0 and arr[nx][ny] == 1 :
                q.append([nx, ny])
                vis[nx][ny] = n
                cnt+=1
    ans.append(cnt)
k = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(k)]
vis = [[0 for _ in range(len(arr))] for _ in range(k)]
r, c = len(arr), k
q = deque()
n= 1
ans = []
for i in range(c):
    for j in range(r):
        if arr[i][j] == 1 and vis[i][j] == 0:
            q.append([i, j])
            vis[i][j] = n
            bfs(n)
            n+=1
print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])