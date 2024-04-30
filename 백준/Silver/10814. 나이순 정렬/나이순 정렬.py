import sys
input = sys.stdin.readline
n = int(input())
l =[]
for _ in range(n):
    li = list(input().split())
    l.append(li)
for i in range(n):
    l[i][0] = int(l[i][0])
l.sort(key=lambda x: x[0])
for i in range(len(l)):
    print(l[i][0], l[i][1])