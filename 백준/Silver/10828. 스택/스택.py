import sys
n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        arr.append(int(order[1]))
    elif order[0] == 'top':
        if len(arr) > 0:
            print(arr[-1])
        else:
            print('-1')
    elif order[0] == 'size':
        print(len(arr))
    elif order[0] == 'pop':
        if len(arr) > 0:
            print(arr.pop())
        else:
            print('-1')
    elif order[0] == 'empty':
        if len(arr) > 0:
            print(0)
        else:
            print(1)