import sys

n = int(sys.stdin.readline())
l = list(map(int,input().split()))
stack = []
turn = 1
for student in l:
    stack.append(student)
    while stack and stack[-1] == turn:
        stack.pop()
        turn+=1
if stack:
    print('Sad')
else:
    print('Nice')