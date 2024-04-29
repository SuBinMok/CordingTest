num = int(input())
l = []
for _ in range(num):
    l.append(input())
a = list(set(l))
a.sort()
a.sort(key = len)
for i in a:
    print(i)