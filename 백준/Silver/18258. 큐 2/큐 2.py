import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    order = sys.stdin.readline().strip()
    if order[:2] == 'pu':
        q.append(order[5:])
    elif order[:2] == 'po':
        if len(q) != 0:
            x = q.popleft()
            print(x)
        else:
            print(-1)
    elif order[:2] == 'si':
        print(len(q))
    elif order[:2] == 'em':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order[:2] == 'fr':
        if len(q) >0:
            print(q[0])
        else:
            print(-1)
    elif order[:2] == 'ba':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)