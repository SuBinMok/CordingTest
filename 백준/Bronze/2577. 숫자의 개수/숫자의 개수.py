a = int(input())
b = int(input())
c = int(input())
abc = str(a*b*c)
l = [0] * 10
for i in abc:
    l[int(i)] += 1
for i in l:
    print(i)