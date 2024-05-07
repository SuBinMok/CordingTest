def solution(spell, dic):
    answer = 2
    for d in dic:
        check = [0] *len(spell)
        for s in range(len(spell)):
            if spell[s] in d:
                check[s] +=1
        if (sum(check) / len(check)) == 1:
            answer = 1            
            
    return answer