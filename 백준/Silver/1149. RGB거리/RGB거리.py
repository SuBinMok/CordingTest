import sys
N = int(sys.stdin.readline())
house = [[0, 0, 0] for _ in range(N)]
d = [[0, 0, 0] for _ in range(N)]
for i in range(N):
    R, G, B = map(int, sys.stdin.readline().split())
    house[i][0] = R
    house[i][1] = G
    house[i][2] = B
d[0][0] = house[0][0]
d[0][1] = house[0][1]
d[0][2] = house[0][2]
for i in range(1, N):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + house[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + house[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + house[i][2]

print(min(d[N-1][0], d[N-1][1], d[N-1][2]))