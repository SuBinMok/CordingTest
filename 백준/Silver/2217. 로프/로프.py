import sys
n = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(n)]
rope = sorted(rope, reverse=True)
kg = []
for i in range(n):
    kg.append(rope[i]*(i+1))

print(max(kg))