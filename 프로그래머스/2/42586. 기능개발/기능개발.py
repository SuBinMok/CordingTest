from collections import deque
from math import ceil
def solution(progresses, speeds):
    answer = []
    temp = 0
    day = deque(ceil((100 - i)/j) for i, j in zip(progresses, speeds)) #남은 일수 계산
    while day:
        d = day.popleft() #우선 순위가 왼 => 오 방향. 왼쪽에 있는 값을 꺼냄.
        if d > temp: #꺼낸 값이 temp보다 크면(이전에 꺼낸 값이 방금 꺼낸 값보다 작음)
            answer.append(1)
            temp = d
        else: # 꺼낸 값이 temp보다 작거나 같으면 한번에 배포할 수 있는 갯수가 됨
            answer[-1] += 1
    return answer