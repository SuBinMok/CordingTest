num = input()
l =[]
for i in range(len(num)):
    l.append(int(num[i]))
l.sort(reverse=True)

for i in range(len(num)):
    print(l[i], end='')