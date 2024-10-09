number = str(input())
l = [0] * 10
c = 0
for i in number:
    l[int(i)] += 1
    if int(i) == 9 or int(i) == 6:
        c +=1
l[6] = int((c+1)/2)
l[9] = int((c+1)/2)
print(max(l))