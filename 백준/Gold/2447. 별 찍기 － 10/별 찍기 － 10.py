import sys

def func(n):
    if n == 1:
        return ["*"]
    star = func(n//3)
    l = []
    for  s in star:
        l.append(s*3)
    for s in star:
        l.append(s+' '*(n//3)+s)
    for s in star:
        l.append(s*3)
    return l

n = int(sys.stdin.readline())
print('\n'.join(func(n)))