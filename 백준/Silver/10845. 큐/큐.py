from collections import deque
import sys
n = int(sys.stdin.readline())
arr = deque()
for _ in range(n):
    order = list(map(str, sys.stdin.readline().split()))
    if order[0] == 'push':
        arr.append(order[1])
    elif order[0] == 'pop':
        if len(arr) != 0:
            print(arr.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(arr))
    elif order[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(arr) > 0:
            print(arr[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(arr) > 0:
            print(arr[-1])
        else:
            print(-1)

