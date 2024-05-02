import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
q = deque(i+1 for i in range(n))
turn = 1
print("<", end="")
while q:
    if len(q) == 1:
        x = q.popleft()
        print(f"{x}>")
        break
    if turn != m:
        x = q.popleft()
        q.append(x)
        turn+=1
    else:
        x = q.popleft()
        print(f"{x},", end=" ")
        turn = 1