import sys
from collections import deque
n, m, k = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
vis = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
q = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs():
    if n == 1 and m == 1:
        return 1
    q.append([0, 0, 0])
    vis[0][0][0] = 1

    while q:
        k_count, x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if nx == n - 1 and ny == m - 1:
                    return vis[k_count][x][y] + 1
                if matrix[nx][ny] == 0 and vis[k_count][nx][ny] == 0:
                    vis[k_count][nx][ny] = vis[k_count][x][y]+1
                    q.append([k_count, nx, ny])
                if matrix[nx][ny] == 1:
                    if k_count < k:
                        if vis[k_count+1][nx][ny] == 0:
                            vis[k_count+1][nx][ny] = vis[k_count][x][y]+1
                            q.append([k_count+1, nx, ny])

    return -1

print(bfs())