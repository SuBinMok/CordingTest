import sys

a = sys.stdin.readline()
l = []
for _ in range(int(a)):
    n = sys.stdin.readline().split()
    if n[0] == '1':
        l.append(n[1])
    elif n[0] == '2':
        if l:
            print(l.pop())
        else:
            print(-1)
    elif n[0] == '3':
        print(len(l))
    elif n[0] == '4':
        if l:
            print(0)
        else:
            print(1)
    elif n[0] == '5':
        if len(l) != 0:
            print(l[-1])
        elif len(l) == 0:
            print(-1)