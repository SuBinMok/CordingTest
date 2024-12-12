import sys
from collections import deque
case = int(sys.stdin.readline())


def bfs(arr, q, visit):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx < n and 0 <= ny< m and arr[nx][ny] == 1 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append([nx, ny])

for _ in range(case):
    n, m, k = map(int, sys.stdin.readline().split())
    arr = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    q = deque()
    c = 0
    a = 0
    while True:
        a+=1
        x, y = map(int, sys.stdin.readline().split())
        arr[x][y] = 1
        if a == k:
            break
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visit[i][j] == 0:
                visit[i][j] = 1
                q.append([i, j])
                bfs(arr, q, visit)
                c += 1
    print(c)