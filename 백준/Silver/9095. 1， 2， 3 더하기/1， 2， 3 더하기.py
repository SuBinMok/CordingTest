import sys
R = int(sys.stdin.readline())
D = [999]*12
D[1] = 1
D[2] = 2
D[3] = 4

for i in range(4, 12):
    D[i] = D[i-1] + D[i-2] + D[i-3]

for _ in range(R):
    N = int(sys.stdin.readline())
    print(D[N])