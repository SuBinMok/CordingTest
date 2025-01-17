import sys
from collections import deque

r =  int(sys.stdin.readline())
d = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]


def bfs(N, q, field, gx, gy):
    while q:
        x, y = q.popleft()
        if x == gx and y == gy:
            return field[x][y] - 1
        for i, j in d:
            nx = x + i
            ny = y + j
            if 0 <= nx < N and 0 <= ny < N and field[nx][ny] == 0:
                q.append([nx, ny])
                field[nx][ny] = field[x][y] + 1

for _ in range(r):
    N = int(sys.stdin.readline())
    sx, sy = map(int, sys.stdin.readline().strip().split())
    gx, gy = map(int, sys.stdin.readline().strip().split())
    q = deque()
    field = [[0] * N for _ in range(N)]

    q.append([sx, sy])
    field[sx][sy] = 1
    print(bfs(N, q, field, gx, gy))
