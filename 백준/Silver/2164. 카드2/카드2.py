from collections import deque
import sys
n = int(sys.stdin.readline())
arr = deque()
for i in range(n):
    arr.append(i+1)
while 1:
    if len(arr) == 1:
        print(arr.popleft())
        break
    else:
        arr.popleft()
        arr.append(arr.popleft())