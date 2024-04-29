num = int(input())
l = []
for _ in range(num):
    l.append(list(map(int, input().split())))

l.sort(key = lambda x:(x[1], x[0]))
for i in range(num):
    print(l[i][0], l[i][1])