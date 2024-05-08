from collections import deque
def solution(s):
    q = deque()
    for i in s:
        if i == '(':
            q.append(i)
        elif i == ')' and len(q) > 0:
            q.popleft()
        elif i == ')' and len(q) == 0:
            return False
    if len(q) != 0:
        return False
    else:
        return True