from collections import deque
def solution(cards1, cards2, goal):
    answer = 'Yes'
    c1 = deque(cards1)
    c2 = deque(cards2)
    l = []
    for g in goal:
        if c1 and g == c1[0]:
            l.append(c1.popleft())
        elif c2 and g == c2[0]:
            l.append(c2.popleft())
            
    if l != goal:
        answer = 'No'
    return answer