n, m = map(int, input().split())
a, b = [], []
for _ in range(n):
    s = input().split()
    a.append(s)
for _ in range(n):
    s = input().split()
    b.append(s)
for i in range(n):
    for j in range(m):
        print(int(a[i][j])+int(b[i][j]), end=" ")
    print()