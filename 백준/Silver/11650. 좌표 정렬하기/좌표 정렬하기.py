num = int(input())
l = []
for _ in range(num):
    l.append(list(map(int, input().split())))
l.sort()
for i in range(num):
    print(l[i][0], l[i][1])