import sys
from collections import deque
MAX = 100001
s, bro = map(int, sys.stdin.readline().split())
visited = [-1] * MAX
path = [-1] * MAX
answer = []
def bfs():
    q = deque()
    q.append(s)
    visited[s] += 1

    while q:
        x = q.popleft()
        l = [x-1, x+1, x*2]
        if x == bro:
            p = []
            temp = x
            print(visited[x])
            while temp != -1:
                p.append(temp)
                temp=path[temp]
            print(*(p[::-1]))
            return
        for nx in l:
            if 0 <= nx < MAX and visited[nx] == -1:
                q.append(nx)
                visited[nx]=visited[x]+1
                path[nx] = x


bfs()