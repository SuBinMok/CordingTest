import sys
input = sys.stdin.readline
l, s = map(int, input().split())
NoseeNolisten = {}
nsnl = []
for _ in range(l):
    NoseeNolisten[input().rstrip()] = 1
for _ in range(s):
    inpu = input().rstrip()
    if inpu not in NoseeNolisten:
        NoseeNolisten[inpu] = 1
    elif NoseeNolisten[inpu] == 1:
        nsnl.append(inpu)
res = sorted(nsnl)
print(len(nsnl))
for i in res:
    print(i)