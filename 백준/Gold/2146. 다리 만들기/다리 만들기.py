import sys
from collections import deque

n = int(sys.stdin.readline())
island = [list(map(int, input().split())) for _ in range(n)]
island_coords = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False]*n for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(n):
        if island[i][j] == 1 and not visited[i][j]:
            q = deque([(i, j)])
            visited[i][j] = True
            island[i][j] = cnt
            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if island[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            island[nx][ny] = cnt
            cnt+= 1

def bridge(island_num):
    q = deque()
    dist = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if island[i][j] == island_num:
                dist[i][j] = 0
                q.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if island[nx][ny] > 0 and island[nx][ny] != island_num:
                    return dist[x][y]
                if island[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])
    return float('inf')

ans = float('inf')
for i in range(1, cnt):
    ans = min(ans, bridge(i))

print(ans)