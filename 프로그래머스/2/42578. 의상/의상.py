def solution(clothes):
    answer = 1
    wear_dic = {}
    for cloth, wear in clothes:
        if wear in wear_dic:
            wear_dic[wear].append(cloth)
        else:
            wear_dic[wear] = [cloth]
    for i in wear_dic.keys():
        answer *= (len(wear_dic[i])+1)
    return answer -1