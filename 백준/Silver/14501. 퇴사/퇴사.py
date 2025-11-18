import sys
N = int(sys.stdin.readline())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, sys.stdin.readline().split())

max_profit = 0


def dfs(day, profit):
    global max_profit
    if day >= N:
        max_profit = max(max_profit, profit)
        return
    if day + T[day] <= N:
        dfs(day + T[day], profit + P[day])
    dfs(day + 1, profit)


dfs(0, 0)
print(max_profit)