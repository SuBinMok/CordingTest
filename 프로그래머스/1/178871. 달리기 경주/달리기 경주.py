def solution(players, callings):
    answer = players
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i
    for i in callings:
        idx = dic[i]
        dic[i] -= 1
        dic[players[idx-1]] += 1
        answer[idx], answer[idx-1] = answer[idx-1], answer[idx]
    return answer