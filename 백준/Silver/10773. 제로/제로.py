import sys

a = sys.stdin.readline()
l = []
for _ in range(int(a)):
    num = int(sys.stdin.readline())
    if num != 0:
        l.append(int(num))
    elif num == 0:
        l.pop()
print(sum(l))