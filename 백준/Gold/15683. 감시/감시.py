import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
office = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# east, south, west, north
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}
def check_in(x, y):
    return x < 0 or x >= n or y < 0 or y >= m
def init():
    cctv = []
    answer = 0
    for i in range(n):
        for j in range(m):
            if office[i][j] != 6 and office[i][j] != 0:
                cctv.append([i, j, office[i][j]])
            if office[i][j] == 0:
                answer += 1
    return cctv, answer
cctv, answer = init()
def rotation(x, y, d_list, co):
    for d in d_list: # 회전하면서
        nx = x
        ny = y
        while True: # 같은 줄에 있는 0 조건에 안걸린다면 X로 바꿈
            nx += dx[d]
            ny += dy[d]
            if check_in(nx, ny) or co[nx][ny] == 6:
                break
            if co[nx][ny] != 0:
                continue
            co[nx][ny] = "X"

def zero_cnt(co):
    global answer
    cnt = 0
    for i in co:
        cnt += i.count(0)
    answer = min(answer, cnt)
def dfs(lv, office):
    copy_office = [[j for j in office[i]] for i in range(n)]
    if lv == len(cctv): # lv : 확인하고 잇는 cctv, 마지막 cctv까지 다 봣으면
        zero_cnt(copy_office)
        return # 이전 상태로 ㄱㄱ

    x, y, num = cctv[lv]
    for d in direction[num]:
        rotation(x, y, d, copy_office)
        dfs(lv+1, copy_office)
        copy_office = [[j for j in office[i]]for i in range(n)]


dfs(0, office)

print(answer)