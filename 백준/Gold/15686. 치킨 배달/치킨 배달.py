import sys
from itertools import combinations
n, M = map(int, sys.stdin.readline().split()) # 행렬 크기 n, 치킨집 갯수
gido = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]# 1 집, 2 치킨가게

chickin = [] # 치킨가게 위치 저장
house = [] # 집 위치 저장

for i in range(n): #완전 탐색 하여 집과 치킨 가게 위치를 저장함
    for j in range(n):
        if gido[i][j] == 1:
            house.append([i, j])
        if gido[i][j] == 2:
            chickin.append([i, j])

result = 99999999
for selected_chickin in combinations(chickin, M):
    current_dist = 0
    for hr, hc in house:
        house_min_dist = float('inf')
        for cr, cc in selected_chickin:
            dist = abs(hr-cr)+abs(hc-cc)
            house_min_dist = min(house_min_dist, dist)
        current_dist += house_min_dist
    result = min(result, current_dist)
print(result)