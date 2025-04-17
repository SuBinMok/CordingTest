import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
l, r = 0, 0
answer = float('inf')
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

while r < n:
    t = arr[r] - arr[l]
    if t >= m:
        answer = min(answer, t)
        l+=1
    else:
        r+=1
    if l ==r:
        r+=1
print(answer)