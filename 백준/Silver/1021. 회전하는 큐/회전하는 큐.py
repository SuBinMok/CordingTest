from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
want = list(map(int, sys.stdin.readline().split()))
arr = deque([i+1 for i in range(n)])
c = 0
for i in want:
    while 1:
        if arr[0] == i:
            arr.popleft()
            break
        else:
            if arr.index(i) <= len(arr)//2:
                arr.append(arr.popleft())
                c +=1
            else:
                arr.appendleft(arr.pop())
                c+=1
print(c)