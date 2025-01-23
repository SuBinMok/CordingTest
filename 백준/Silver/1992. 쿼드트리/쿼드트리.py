import sys

def func(r, c, n):
    cur = field[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if cur != field[i][j]:
                n //= 2
                print("(", end="")
                func(r, c, n)
                func(r, c+n, n)
                func(r+n, c, n)
                func(r+n, c+n, n)
                print(")", end="")
                return

    print(cur, end="")


    return

n = int(sys.stdin.readline())
field = [[i for i in str(sys.stdin.readline())] for _ in range(n)]
func(0, 0, n)

# ((110(0101))(0010)1(0001))
# ((110(0101))(0010)1(0001))