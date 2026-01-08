import sys

# 재귀 한도를 늘려주어야 RecursionError를 피할 수 있습니다.
sys.setrecursionlimit(10 ** 6)

def dfs(current):
    global result
    visited[current] = True
    path.append(current)
    next = selection[current]
    if not visited[next]:
        dfs(next)
    else:
        if not finished[next]:
            cycle_members = path[path.index(next):]
            result += len(cycle_members)
    finished[current] = True

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    selection = [0] + list(map(int, sys.stdin.readline().split()))

    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    result = 0  # 팀에 속한 학생 수

    for i in range(1, n + 1):
        if not visited[i]:
            path = []  # 현재 DFS에서 지나온 경로 저장
            dfs(i)

    # 전체 학생 수 - 팀에 속한 학생 수 = 팀이 없는 학생 수
    print(n - result)