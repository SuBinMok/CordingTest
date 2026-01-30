import sys

n = int(sys.stdin.readline())

dp = [0] * 1001 
if n== 1:
    print(1)
    exit()
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])