import sys

def func(n, r, c):
    if n == 0:
        return n
    half = 2**(n-1)
    if r < half and c < half: #1
        return func(n-1, r, c)
    elif r < half  and c >= half:#2
        return half*half+func(n-1, r, c-half)
    elif r >= half and c < half:#3
        return 2*half*half+func(n-1, r-half, c)
    elif r >= half and c >= half:#4
        return 3*half*half+func(n-1, r-half, c-half)

n, r, c = map(int, sys.stdin.readline().split())
print(func(n, r, c))