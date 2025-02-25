import sys

n, t = map(int, sys.stdin.readline().split())
dic = {}
for i in range(n):
    name = str(sys.stdin.readline().rstrip())
    dic[str(i+1)] = name
    dic[name] = str(i+1)

for _ in range(t):
    print(dic[str(sys.stdin.readline().rstrip())])