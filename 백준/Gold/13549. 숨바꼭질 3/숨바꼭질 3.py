import sys
from collections import deque

# N: 시작 위치, K: 목표 위치
n, k = map(int, sys.stdin.readline().split())
MAX = 100001 # 0부터 100,000까지

# 방문 여부와 시간을 동시에 저장 (초기값 -1)
dist = [-1] * MAX

def bfs():
    q = deque([n])
    dist[n] = 0 # 시작 위치 0초
    
    while q:
        x = q.popleft()
        
        # 목표 지점에 도달하면 시간 반환
        if x == k:
            return dist[x]
        
        # 1. 순간이동 (0초): 큐의 맨 앞에 넣음 (우선순위 높음)
        if 0 <= x * 2 < MAX and dist[x * 2] == -1:
            dist[x * 2] = dist[x] # 시간은 그대로
            q.appendleft(x * 2)
            
        # 2. 걷기 (1초): 큐의 맨 뒤에 넣음
        for nx in (x - 1, x + 1):
            if 0 <= nx < MAX and dist[nx] == -1:
                dist[nx] = dist[x] + 1 # 시간 1초 증가
                q.append(nx)

print(bfs())