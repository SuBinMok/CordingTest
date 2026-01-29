import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    matrix = [input().rstrip() for _ in range(n)]

    if n == 1 and m == 1:
        print(1)
        return

    vis = [[[-1] * m for _ in range(n)] for _ in range(k + 1)]
    
    q = deque([(0, 0, 0, 1)]) # kc, x, y, dist
    vis[0][0][0] = 1
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while q:
        kc, x, y, dist = q.popleft()
        
        # 낮밤 판정 (dist가 홀수면 낮, 짝수면 밤)
        is_day = dist % 2 
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                # 목적지 도착 시 즉시 종료
                if nx == n - 1 and ny == m - 1:
                    print(dist + 1)
                    return

                # 1. 빈 공간일 때
                if matrix[nx][ny] == '0':
                    if vis[kc][nx][ny] == -1:
                        vis[kc][nx][ny] = dist + 1
                        q.append((kc, nx, ny, dist + 1))
                
                # 2. 벽일 때
                elif kc < k and vis[kc + 1][nx][ny] == -1:
                    if is_day: # 낮이면 바로 부수기
                        vis[kc + 1][nx][ny] = dist + 1
                        q.append((kc + 1, nx, ny, dist + 1))
                    else: # 밤이면 제자리 기다리기
                        # '낮에 부수기 위해 기다리는 상태'를 별도로 체크
                        if vis[kc][x][y] < dist + 1: 
                            vis[kc][x][y] = dist + 1
                            q.append((kc, x, y, dist + 1))

    print(-1)

solve()