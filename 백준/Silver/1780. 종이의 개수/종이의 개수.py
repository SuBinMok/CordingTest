import sys

result = {-1: 0, 0: 0, 1: 0}
def func(r, c, n):
    cur = field[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if cur != field[i][j]:
                n //= 3
                func(r, c, n)
                func(r, c+n, n)
                func(r, c+(2*n), n)
                func(r+n, c, n)
                func(r+n, c+n, n)
                func(r+n, c+(2*n), n)
                func(r+(2*n), c, n)
                func(r+(2*n), c+n, n)
                func(r+(2*n), c+(2*n), n)
                return
    result[cur]+= 1
    return

n = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
func(0, 0, n)

for i in result.values():
    print(i)