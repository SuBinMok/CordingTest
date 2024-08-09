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
    
    if a[0] == a[1] == a[2]:
        return [1, 2, 3]
    elif a[0] == a[1] and a[0] > a[2]:
        return [1, 2]
    elif a[0] == a[2] and a[0] > a[1]:
        return [1, 3]
    elif a[1] == a[2] and a[1] > a[0]:
        return [2, 3]
    elif a[0] > a[1] and a[0] > a[2]:
        return [1]
    elif a[1] > a[0] and a[1] > a[2]:
        return [2]
    elif a[2] > a[1] and a[2] > a[0]:
        return [3]