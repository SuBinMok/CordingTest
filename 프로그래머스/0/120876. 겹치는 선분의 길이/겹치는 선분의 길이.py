def solution(lines):
    answer = 0
    c = [0] * 201
    for i, j in lines:
        print(i, j)
        for k in range(j - i):
            c[k+100+i] += 1
    for i in c:
        if i >= 2:
            answer+=1
    return answer
