def solution(answers):
    a = [0, 0, 0]
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, j in enumerate(answers):
        if j == p1[i%len(p1)]:
            a[0] +=1
        if j == p2[i%len(p2)]:
            a[1] +=1
        if j == p3[i%len(p3)]:
            a[2] +=1
    
    for i, j in enumerate(a):
        if j == max(a):
            answer.append(i+1)
    return answer