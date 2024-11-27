import sys as s
n = int(s.stdin.readline().strip())
building = [0]*n
for i in range(n):
    building[i] = int(s.stdin.readline().strip())
result = 0
stack = []
for c in building:
    while stack and stack[-1] <= c: #스택이 채워져있고, 스택 마지막에 들어온 애가 c보다 작으면
        stack.pop() #그런 스택만 제거
    result += len(stack)
    stack.append(c)
print(result)