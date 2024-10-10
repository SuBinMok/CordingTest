from collections import deque

people, n = map(int, input().split())
r = deque()
for i in range(1, people+1): r.append(i)
c = 1
answer = []

while r:
    for _ in range(n-1):
        r.append(r.popleft())
    answer.append(r.popleft())

print(str(answer).replace("[", "<").replace("]",">"))