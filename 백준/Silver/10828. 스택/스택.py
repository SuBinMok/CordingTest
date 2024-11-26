import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    x = sys.stdin.readline().split()
    if x[0] == 'push':
        arr.append(int(x[1]))
    elif x[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else: 
            print(arr.pop())
    elif x[0] == 'size':
        print(len(arr))
    elif x[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == 'top':
        if len(arr) != 0:
            print(arr[-1])
        else:
            print(-1)