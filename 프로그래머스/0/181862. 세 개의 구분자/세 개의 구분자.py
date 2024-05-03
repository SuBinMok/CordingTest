def solution(myStr):
    answer = []
    temp = ''
    for i in range(len(myStr)):
        if myStr[i] != "a" and myStr[i]!="b" and myStr[i]!="c":
            temp+=myStr[i]
        else:
            if len(temp) > 0:
                answer.append(temp)
                temp = ''
        if len(myStr) - 1 == i:
           if len(temp) > 0:
                answer.append(temp)
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer