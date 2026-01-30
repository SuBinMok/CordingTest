import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
dp = [0]*(n+1)

for i in range(1, n+1):
    dp[i] = dp[i-1] + l[i-1]

for _ in range(m):
    s1, s2 = map(int, sys.stdin.readline().split())
    print(dp[s2] - dp[s1-1])
    