from collections import deque
def solution(s):
    queue = deque()
    for i in s:
        if i == "(":
            queue.append(i)
        elif i == ")" and len(queue) > 0:
            queue.popleft()
        elif i == ")" and len(queue) == 0:
            return False
    if len(queue) != 0:
        return False
    else:
        return True