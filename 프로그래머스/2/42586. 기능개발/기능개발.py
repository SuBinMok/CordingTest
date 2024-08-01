from math import ceil
def solution(progresses, speeds):
    answer = []
    temp = 0
    for i in range(len(progresses)):
        speeds[i] = ceil((100 - progresses[i]) / speeds[i])
    while speeds:
        s = speeds.pop(0)
        if s > temp :
            answer.append(1)
            temp = s
        else:
            answer[-1] +=1
    return answer