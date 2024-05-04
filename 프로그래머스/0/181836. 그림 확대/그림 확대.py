def solution(picture, k):
    answer = []
    temp = ""
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            for _ in range(k):
                temp+=picture[i][j]
        for _ in range(k):
            answer.append(temp)
        temp = ""
    return answer
