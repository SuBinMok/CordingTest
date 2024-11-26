import sys
r = int(input())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []
for i in range(r):
    while stack:
        if stack[-1][1] >= arr[i]:
            answer.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append((i, arr[i]))
for i in answer:
    print(i, end = ' ')