def solution(n):
    answer = 0
    for i in range(n):
        while answer % 3 == 0 or "3" in str(answer):
            answer+=1
        answer +=1
    return answer-1