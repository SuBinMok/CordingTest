def solution(emergency):
    answer = []
    temp = sorted(emergency, reverse = True)
    for i in emergency:
        for j in range(len(temp)):
            if i == temp[j]:
                answer.append(j+1)
    return answer