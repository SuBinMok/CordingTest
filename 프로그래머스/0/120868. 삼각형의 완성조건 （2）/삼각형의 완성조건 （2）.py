def solution(sides):
    answer = 0
    for i in range(max(sides)-1):
        if i + min(sides) >= max(sides):
            answer+=1
    for i in range(max(sides), sum(sides)):
        answer +=1
    return answer