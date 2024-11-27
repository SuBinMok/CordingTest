import sys as s

n = int(s.stdin.readline().strip())
line = list(map(int, s.stdin.readline().split()))
stack = []
result = [-1]*n

for cur in range(n):
    while stack and line[stack[-1]] < line[cur]:
        result[stack.pop()] = line[cur]
    stack.append(cur)
for i in range(n):
    print(result[i], end=' ')