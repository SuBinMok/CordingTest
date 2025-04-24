import sys
from collections import deque

total_repeat = int(sys.stdin.readline())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def fire_bfs(fq, graph, m, n, visited_f):
    while fq:
        x, y = fq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if graph[nx][ny] != '#' and visited_f[nx][ny] == 0:
                visited_f[nx][ny] = visited_f[x][y] + 1
                fq.append([nx, ny])

def bfs(sq, graph, m, n, visited_s, visited_f):
    while sq:
        x, y = sq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != '#' and visited_s[nx][ny] == 0:
                    if not visited_f[nx][ny] or visited_f[nx][ny] > visited_s[x][y]+1:
                        visited_s[nx][ny] = visited_s[x][y]+1
                        sq.append([nx, ny])
            else:
                return visited_s[x][y]
    return "IMPOSSIBLE"

while total_repeat > 0:
    total_repeat -= 1
    n, m = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(m):
        graph.append(list(map(str, sys.stdin.readline().rstrip())))
    fire = deque()
    sq = deque()
    visited_f = [[0]*n for _ in range(m)]
    visited_s = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if graph[i][j] == '@':
                sq.append([i, j])
                visited_s[i][j] = 1
            if graph[i][j] == '*':
                fire.append([i, j])
                visited_f[i][j] = 1
    fire_bfs(fire, graph, n, m, visited_f)
    print(bfs(sq, graph, n, m, visited_s, visited_f))