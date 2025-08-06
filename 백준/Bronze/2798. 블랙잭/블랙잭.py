import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0
cnt = 1
temp = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and i != k and j !=k and answer <=  arr[i]+arr[j]+arr[k] <= M:
                answer = arr[i] + arr[j] + arr[k]
print(answer)