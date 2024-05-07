def solution(s):
    answer = 0
    l = []
    s = s.split()
    for i in s:
        if i != 'Z':
            l.append(int(i))  
        else:
            l.pop()
    answer = sum(l)
    return answer