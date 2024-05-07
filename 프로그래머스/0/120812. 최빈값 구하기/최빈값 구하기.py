def solution(array):
    t = [0] * 1001
    for i in array:
        t[i] += 1
    m = max(t)
    if t.count(m) > 1:
        return -1
    else:
        return t.index(m)