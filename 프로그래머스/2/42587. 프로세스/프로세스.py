import copy
from collections import deque
def solution(priorities, location):
    answer =  0
    q = deque(enumerate(priorities)) #같은 값을 가진 우선 순위가 있으므로 enumerate를 사용해 구분.
    while q:
        _, m = max(q, key = lambda x: x[1])
        l, now = q.popleft() # location과 비교할 l, now는 현재 우선 순위
        if now < m:
            q.append((l, now))
        else:
            answer+=1
            if l == location:
                break
    return answer