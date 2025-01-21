import sys
R = int(sys.stdin.readline())
s = [0] * R
d = [[0, 0] for i in range(R)]
for i in range(R):
    s[i] = int(sys.stdin.readline())


if R == 1:
    print(s[0])
else:
    d[0][0] = s[0]
    d[0][1] = 0
    d[1][0] = s[1]
    d[1][1] = s[0] + s[1]
    for i in range(2, R):
        d[i][0] = max(d[i-2][0], d[i-2][1]) + s[i]
        d[i][1] = d[i-1][0] + s[i]

    print(max(d[R-1][0], d[R-1][1]))