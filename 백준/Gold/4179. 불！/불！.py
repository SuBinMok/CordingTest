import sys
from collections import deque

def fire():
    while fq:
        fx, fy = fq.popleft()
        for i in range(4):
            nfx = fx + dx[i]
            nfy = fy + dy[i]
            if not (0 <= nfx < r and 0 <= nfy < c):
                continue
            if mirro[nfx][nfy] != '#' and visited_F[nfx][nfy] == 0:
                visited_F[nfx][nfy] = visited_F[fx][fy]+1
                fq.append([nfx, nfy])
def jihun():
    while jq:
        jx, jy = jq.popleft()
        for i in range(4):
            njx = jx + dx[i]
            njy = jy + dy[i]
            if 0 <= njx < r and 0 <= njy < c:
                if mirro[njx][njy] != '#' and visited_J[njx][njy] == 0:
                    if not visited_F[njx][njy] or visited_F[njx][njy] > visited_J[jx][jy] + 1:
                        visited_J[njx][njy] = visited_J[jx][jy]+1
                        jq.append([njx, njy])
            else:
                return visited_J[jx][jy]

    return "IMPOSSIBLE"
r, c = map(int, sys.stdin.readline().split())
mirro = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
visited_J = [[0]*c for _ in range(r)]
visited_F = [[0]*c for _ in range(r)]
jq = deque()
fq = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(r):#초기위치
    for j in range(c):
        if mirro[i][j] == 'J':
            jq.append([i, j])
            visited_J[i][j] = 1
        elif mirro[i][j] == 'F':
            fq.append([i, j])
            visited_F[i][j] = 1
fire()
print(jihun())