import sys

N, M = map(int, sys.stdin.readline().split())
secret = {}
for _ in range(N):
    site, password = map(str, sys.stdin.readline().split())
    secret[site] = password

for _ in range(M):
    site = str(sys.stdin.readline().rstrip())
    print(secret[site])