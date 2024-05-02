import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque(i+1 for i in range(n))
l = list(map(int, sys.stdin.readline().rstrip().split()))
x = q.popleft()  # 첫번째 pop
print(x, end=" ")
while q:
    a = l[x-1]
    temp = 1
    if a > 0: #양수
        for i in range(a-1):
            e = q.popleft()
            q.append(e)
        temp = 0
    elif a < 0: #음수
        for i in range(abs(a+1)):
            e = q.pop()
            q.appendleft(e)
        temp = 0
    if temp == 0:
        if a > 0:
            e = q.popleft()
            x = e
            print(e, end=" ")
        elif a < 0:
            e = q.pop()
            x = e
            print(e, end=" ")