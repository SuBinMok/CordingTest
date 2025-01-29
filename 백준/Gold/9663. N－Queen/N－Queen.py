import sys
n = int(sys.stdin.readline())
isused1 = [0]*n
isused2 = [0]*n*n
isused3 = [0]*n*n
cnt = 0

def func(cur):
    global cnt
    if cur == n:
        cnt += 1
        return
    for i in range(n):
        if isused1[i] or isused2[i+cur] or isused3[n-1+cur-i]:
            continue
        isused1[i] = 1
        isused2[cur+i] = 1
        isused3[n-1+cur-i] = 1
        func(cur+1)
        isused1[i] = 0
        isused2[cur + i] = 0
        isused3[n - 1 + cur - i] = 0

func(0)
print(cnt)