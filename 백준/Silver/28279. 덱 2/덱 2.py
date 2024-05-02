import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    t = sys.stdin.readline().rstrip()
    if t[0] == '1':
        q.appendleft(t[2:])
    elif t[0] == '2':
        q.append(t[2:])
    elif t[0] == '3':
        if len(q) > 0:
            x = q.popleft()
            print(x)
        else:
            print(-1)
    elif t[0] == '4':
        if len(q) > 0:
            x = q.pop()
            print(x)
        else:
            print(-1)
    elif t[0] == '5':
        print(len(q))
    elif t[0] == '6':
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif t[0] == '7':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif t[0] == '8':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)