"""
자기 자신은 항상 자기 자신과 연결이 되어 있음. computers[i][i] 언제나 1 
다른 컴과 연결이 되어 있는지 보기 위해서는 computers[i][j] 가 1인지 확인해야함. 
if computers[i][j] == 1 cnt +=1 => if cnt == len(computers) => 모든 pc가 연결됨 => return 1
if 이전 cnt = len(computers)-1 현재 cnt = 1 => return 이전 cnt
"""
from collections import deque
def solution(n, computers):
    answer = 0
    q = deque()
    visited = [[0]*n]*n
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and computers[i][j] == 1:
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    visited[x][y] = 1
                    for k in range(n):
                        if visited[x][k] == 0 and computers[x][k] == 1:
                            visited[x][k] = 1
                            q.append([k, x])
                    
                answer += 1
    return answer