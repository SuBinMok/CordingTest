import sys
from collections import deque
m, n= map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()
c = 0
a = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx < n and 0 <= ny< m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx, ny])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j])
bfs()
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    c= max(c, max(i))
print(c-1)
