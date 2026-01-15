import sys
from collections import deque

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

hx = [-2, -1, 1, 2, -2, -1, 1, 2]
hy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    visited = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]
    q = deque([(0,0, 0)])
    visited[0][0][0] = 0
    while q:
        x, y, spent_k = q.popleft()
        if x == h-1 and y == w -1 :
            return visited[x][y][spent_k]
        if k > spent_k:
            for i in range(8):
                nx, ny = x+hx[i], y+hy[i]
                if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 0:
                    if visited[nx][ny][spent_k+1] == -1:
                        q.append((nx, ny, spent_k+1))
                        visited[nx][ny][spent_k+1] = visited[x][y][spent_k] + 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != 1:
                if visited[nx][ny][spent_k] == -1:
                    q.append((nx, ny, spent_k))
                    visited[nx][ny][spent_k] = visited[x][y][spent_k] + 1

    return -1
if w == 1 and h == 1:
    print(0)
else:
    print(bfs())