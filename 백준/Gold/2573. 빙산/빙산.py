import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
ice = []
ice_coords = [] # 빙산이 있는 좌표만 저장할 리스트

for r in range(n):
    row = list(map(int, input().split()))
    ice.append(row)
    for c in range(m):
        if row[c] > 0:
            ice_coords.append((r, c)) # 빙산 위치 저장

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def get_island_count(current_ice):
    if not current_ice:
        return 0
    
    visited = [[False] * m for _ in range(n)]
    count = 0
    
    for r, c in current_ice:
        if ice[r][c] > 0 and not visited[r][c]:
            # BFS 시작
            q = deque([(r, c)])
            visited[r][c] = True
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m:
                        if ice[nx][ny] > 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
            count += 1 
    return count

year = 0
while ice_coords:
    islands = get_island_count(ice_coords)
    
    if islands >= 2:
        print(year)
        break
    
    melt_list = []
    new_ice_coords = []
    
    for r, c in ice_coords:
        sea_cnt = 0
        for i in range(4):
            nx, ny = r + dx[i], c + dy[i]
            if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] == 0:
                sea_cnt += 1
        melt_list.append((r, c, sea_cnt))
    
    for r, c, cnt in melt_list:
        ice[r][c] = max(0, ice[r][c] - cnt)
        if ice[r][c] > 0:
            new_ice_coords.append((r, c)) 
            
    ice_coords = new_ice_coords
    year += 1

else:
    print(0)