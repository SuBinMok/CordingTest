def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for p in participant:
        dic[hash(p)] = p #hash[p] => 고유 값
        temp += int(hash(p)) #같은 값이 두개 있으면 두번 더하는 것
    for c in completion:
        temp -= hash(c) # completion에 중복된 값이 없으면 temp에는 p에서 더한 중복 값이 남아 있음
    return dic[temp]