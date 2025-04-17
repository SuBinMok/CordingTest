import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
l, r = 0, 0
answer = float('inf')
temp = 0
while r < n:
    temp+=arr[r]
    r+=1
    while temp >= s:
        answer = min(answer, r-l)
        temp -= arr[l]
        l += 1

if answer == float('inf'):
    print(0)
else:
    print(answer)