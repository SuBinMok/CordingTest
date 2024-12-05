import sys
re = int(sys.stdin.readline())
c = 0
for _ in range(re):
    sentence = str(sys.stdin.readline().strip())
    stack = []
    for i in sentence:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        c+=1

print(c)