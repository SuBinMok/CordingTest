import sys

n,m = map(int, sys.stdin.readline().split())
l = list(map(str, sys.stdin.readline().split()))
arr = [0] * n
l.sort()
attend = [0]*m

def valid(password):
    v = ['a', 'e', 'i', 'o', 'u']
    v_cnt = sum(1 for c in password if c in v)
    cnt = len(password) - v_cnt
    return v_cnt >= 1 and cnt >= 2

def func(depth, start):
    if depth == n:
        if valid(arr):
            for i in arr:
                print(i, end='')
            print()
        return

    for i in range(start, m):
         if attend[i] == 0:

             attend[i] = 1
             arr[depth] = l[i]
             func(depth+1, i+1)
             attend[i] = 0

func(0, 0)
