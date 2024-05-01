import sys
input = sys.stdin.readline
a = input().rstrip()
cnt = 0
list_ = []
for i in range(len(a)):
    j = (i+1)%len(a)
    for k in range(len(a)):
        if j == 0:
            list_.append(a[:])
            break
        elif k + j <= len(a):
            list_.append(a[k:k+j])
        else:
            break

print(len(set(list_)))