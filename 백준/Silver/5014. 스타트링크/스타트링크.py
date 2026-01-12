import sys
from collections import deque
F, S, G, U, D = map(int, sys.stdin.readline().split())


def bfs():
    visited = [-1] * (F + 1)
    q = deque([S])
    visited[S] = 0

    while q:
        now = q.popleft()
        if now == G:
            return visited[now]
        for next in (now - D, now + U):
            if 1<=next <= F and visited[next] == -1:
                visited[next] = visited[now] + 1
                q.append(next)
    return "use the stairs"
print(bfs())