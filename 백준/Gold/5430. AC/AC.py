from collections import deque
import sys
T = int(input())

for _ in range(T):
    hamsu = str(input())
    arr_size = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    rev, front, back, flag = 0, 0, len(arr)-1, 0
    if arr_size == 0:
        arr = deque()
    for i in hamsu:
        if i == 'R':
            rev += 1
        elif i == 'D':
            if arr:
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print('error')
                flag = 1
                break
    if flag == 0:
        if rev % 2 == 0:
            print("["+",".join(arr)+"]")
        else:
            arr.reverse()
            print("[" + ",".join(arr) + "]")