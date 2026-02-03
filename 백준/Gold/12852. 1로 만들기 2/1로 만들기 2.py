import sys

n = int(sys.stdin.readline())
dp = [0]*(n+1) # 최소 횟수 기록
pre = [0]*(n+1) # 이전 단계 기록

for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    pre[i] = i-1

    if i % 2 == 0:
        if dp[i] > dp[i//2] + 1:
            dp[i] = dp[i//2] + 1
            pre[i] = i//2
    if i % 3 == 0:
        if dp[i] > dp[i//3] + 1:
            dp[i] = dp[i//3] + 1
            pre[i] = i//3

print(dp[n])

curr = n
while True:
    print(curr, end= ' ')
    if curr == 1: break
    curr = pre[curr]