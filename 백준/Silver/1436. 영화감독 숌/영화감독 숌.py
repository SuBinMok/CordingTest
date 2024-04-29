n = int(input())
l = [0]*n
li = 0
s = 666
while True:
    num = str(s)
    six = 0
    for i in range(len(num)):
        if num[i] == '6':
            six += 1
        elif num[i] != '6':
            six = 0
        if six  >= 3:
            l[li] = int(num)
            li+=1
            break
    s += 1
    if l[n-1] != 0:
        break
print(l[n-1])