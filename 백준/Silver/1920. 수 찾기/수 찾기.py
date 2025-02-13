import sys


n = int(sys.stdin.readline())
a_list = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
b_list = list(map(int, sys.stdin.readline().split()))


def binary(s, e, b):
    if s > e:
        return 0

    now = (s+e)//2
    if b == a_list[now]:
        return 1
    elif b < a_list[now]:
        return binary(s, now-1, b)
    else:
        return binary(now+1, e, b)



for i in b_list:
    s = 0
    e = n - 1
    print(binary(s, e, i))

