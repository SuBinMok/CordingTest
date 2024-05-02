import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque(i+1 for i in range(n))
while q:
    if len(q) == 1:
        x = q.popleft()
        print(x)
        break
    else:
        q.popleft()
        next = q.popleft()
        q.append(next)