def solution(participant, completion):
    dic = {}
    temp = 0
    for p in participant:
        dic[hash(p)] = p
        temp += hash(p)
    for c in completion:
        temp -= hash(c)
    return dic[temp]