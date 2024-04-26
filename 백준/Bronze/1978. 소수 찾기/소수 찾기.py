n = int(input())
l = input().split()
    
for i in range(len(l)):
    cnt = 0
    for j in range(1, int(l[i])+1):
        if int(l[i]) % j == 0:
            cnt += 1
    if int(l[i]) == 1:
        n -= 1
    elif cnt != 2:
        n -= 1
print(n)