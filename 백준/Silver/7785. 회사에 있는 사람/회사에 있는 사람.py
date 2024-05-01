import sys
input = sys.stdin.readline
n = int(input())
dic = {}
for _ in range(n):
    name, inout = map(str, input().split())
    if inout == 'enter':
        dic[name] = True
    else:
        del dic[name]
print("\n".join(sorted(dic.keys(), reverse=True)))