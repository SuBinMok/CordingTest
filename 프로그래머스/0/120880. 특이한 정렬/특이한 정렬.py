def solution(numlist, n):
    answer = []
    result = []
    for i in numlist:
        answer.append([abs(i - n), i])
    answer = sorted(answer)
    for i in range(len(answer)-1):
        if answer[i][0] == answer[i+1][0]:
            temp = answer[i][1]
            answer[i][1] = answer[i+1][1]
            answer[i+1][1] = temp
    for i in range(len(answer))    :
        result.append(answer[i][1])
        
    return result