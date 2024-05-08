def solution(clothes):
    wear = {}
    answer = 1
    for c, w in clothes:
        if w in wear:
            wear[w].append(c) #append로 새 값을 추가할 수 있게 함
        else:
            wear[w] = [c] #리스트 형태로 딕셔너리에 추가해서
    for k in wear.keys():
        answer *= (len(wear[k])+1) # 답은 (dic[key]+1) 크기만큼 곱해나감.
    return answer - 1 