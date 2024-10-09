n = int(input())
l = list(map(int, input().split()))
target = int(input())
nl = [0] * 2000001
count = 0
for i in l:
    t_l = target - i
    if nl[t_l] == 0:
        nl[i] += 1 # 방문 표시
    elif nl[t_l] == 1:
        count += 1
        nl[t_l]+=1
print(count)


