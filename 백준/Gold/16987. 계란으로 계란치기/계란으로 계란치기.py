import sys

n = int(sys.stdin.readline())
egg = []
for _ in range(n):
    egg.append(list(map(int, sys.stdin.readline().split())))

answer = 0

def func(d, cnt):
    global answer
    if d == n: #최근에 든 달걀이 가장 오른쪽이면
        answer = max(answer, cnt)
        return
    if egg[d][0] <= 0: #깨진 달걀을 들 차례이면
        func(d+1, cnt)
        return

    att = 0
    for i in range(n):
        if i == d or egg[i][0] <= 0:
            continue
        egg[i][0] -= egg[d][1]
        egg[d][0] -= egg[i][1]
        crack_i = egg[i][0]<=0
        crack_d = egg[d][0]<=0
        cnt += crack_d+crack_i
        att = 1
        func(d+1, cnt)
        # 복구, 백트래킹
        cnt -= crack_i+crack_d
        egg[i][0] += egg[d][1]
        egg[d][0] += egg[i][1]

    if not att:
        func(d+1, cnt)
        return

func(0, 0)
print(answer)