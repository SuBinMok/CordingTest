def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        x = int(i[s:s+l])
        if x > k:
            answer.append(x)
    return answer