def solution(s):
    answer = ''
    l = sorted(list(set(s)))
    a = [0] *len(l)
    for i in s:
        for j in range(len(l)):
            if i == l[j]:
                a[j]+=1
    for i in range(len(a)):
        if a[i] == 1:
            answer+=l[i]
    return answer