import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    l = list(map(int, sys.stdin.readline().rstrip()))
    arr.append(l)

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
q = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        ax, ay, broken = q.popleft()
        if ax == n - 1 and ay == m - 1:
            return visited[ax][ay][broken]
        for i in range(4):
            nx, ny = ax+dx[i], ay+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny][broken] == 0 :
                    visited[nx][ny][broken] = visited[ax][ay][broken] + 1
                    q.append([nx, ny, broken])
                elif arr[nx][ny] == 1 and broken == 0:
                    if visited[nx][ny][1] == 0:
                        visited[nx][ny][1] = visited[ax][ay][0] + 1
                        q.append([nx, ny, 1])
    return -1

print(bfs())
