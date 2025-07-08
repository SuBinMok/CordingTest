import sys
from collections import deque
m, n, k = map(int, sys.stdin.readline().split())
arr = [[0] * n for _ in range(m)]
for i in range(1, k+1):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())
    for x in range(ly, ry):
        for y in range(lx, rx):
            arr[x][y] = i
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

def bfs(x, y):
    global count
    que = deque()
    que.append([x, y])
    arr[x][y] = 9
    size = 1
    while que:
        ax, ay = que.popleft()
        for i in range(4):
            nx = ax+dx[i]
            ny = ay+dy[i]
            if 0 <= nx < m and 0 <= ny < n  and arr[nx][ny] == 0:
                que.append([nx, ny])
                arr[nx][ny] = 9
                size+=1
    result.append(size)
result = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            bfs(i, j)

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')