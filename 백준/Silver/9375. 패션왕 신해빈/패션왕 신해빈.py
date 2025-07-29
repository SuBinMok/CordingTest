import sys

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    clothes = {}
    result = 1
    M = int(sys.stdin.readline().rstrip())
    for _ in range(M):
        cloth, category = map(str, sys.stdin.readline().split())
        if category not in clothes:
            clothes[category] = 1
        else:
            clothes[category] += 1
    for i in clothes:
        result *= clothes[i] + 1

    print(result-1)