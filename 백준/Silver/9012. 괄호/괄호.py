import sys
re = int(sys.stdin.readline())
for _ in range(re):
    sentence = str(sys.stdin.readline().strip())
    stack = []
    for i in sentence:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
