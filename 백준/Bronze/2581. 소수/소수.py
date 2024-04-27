n = int(input())
m = int(input())
l = []
for i in range(n, m + 1):
    cnt = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0: # 나눠지는 수가 있으면 소수가 이남
                cnt+=1
                break
        if cnt == 0:
            l.append(i)
if len(l) > 0:
    print(sum(l))
    print(min(l))
else:
    print(-1)