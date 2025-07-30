import sys
from collections import deque
N, M, G = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(N)]

#서북동남, 서북, 동북, 동남, 서남
dx = [-1, 0, 1, 0, -1, 1, 1, -1]
dy = [0, -1, 0, 1, -1, -1, 1, 1]
like_dict = {}

def bfs (i, j):
    q = deque()
    q.append([i, j, arr[i][j]])
    while q:
        x, y, s = q.popleft()
        if s in like_dict:
            like_dict[s] +=1
        else:
            like_dict[s] = 1

        if len(s) > 5 : # 1 ≤ 신이 좋아하는 문자열의 길이 ≤ 5
            continue
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == N :
                nx = 0
            elif nx == -1 :
                nx = N - 1
            if ny == M :
                ny = 0
            elif ny == -1:
                ny = M - 1

            q.append([nx, ny, s + arr[nx][ny]])

for i in range(N):
    for j in range(M):
        bfs(i, j)

answer = []
for _ in range(G):
    god_like = str(sys.stdin.readline().rstrip())
    if god_like in like_dict:
        answer.append(like_dict[god_like])
    else:
        answer.append(0)

for i in range(len(answer)):
    print(answer[i])