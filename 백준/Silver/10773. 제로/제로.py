import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0 and len(arr) != 0:
        arr.pop()
    elif num != 0:
        arr.append(num)
print(sum(arr))