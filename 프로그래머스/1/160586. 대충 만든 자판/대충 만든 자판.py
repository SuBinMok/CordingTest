def solution(keymap, targets):
    answer = []
    key_dic = {}
    #딕셔너리, 중복제거.
    for i, key in enumerate(keymap):
        for idx, c in enumerate(key):
            if c not in key_dic:
                key_dic[c] = idx + 1
            else:
                key_dic[c] = min(key_dic[c], idx+1)
    for t in targets:
        cnt = 0
        for c  in t:
            if c in key_dic:
                cnt += key_dic[c]
            else:
                cnt = -1
                break
        answer.append(cnt)
    return answer