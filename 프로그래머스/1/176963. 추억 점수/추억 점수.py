def solution(name, yearning, photo):
    answer = [0 for i in range(len(photo))]
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if photo[i][j] in dic:
                answer[i] += dic[photo[i][j]]
    return answer