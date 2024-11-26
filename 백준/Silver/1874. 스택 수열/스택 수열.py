n = int(input())
arr = []
op = []
flag = True
c = 1
for _ in range(n):
    num = int(input())
    while c <= num:
        arr.append(c)
        op.append('+')
        c +=1
    if arr[-1] == num:
        arr.pop()
        op.append('-')
    else:
        flag = False
        break
if flag == False:
    print("NO")
else:
    for i in op:
        print(i)
        