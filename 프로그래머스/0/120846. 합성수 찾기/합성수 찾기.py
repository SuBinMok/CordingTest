def solution(n):
    answer = 0
    cnt = 0
    for i in range(4, n+1):
        if (i % 2 == 0) and (i > 2):
            cnt += 1
        if (i % 3 == 0) and (i > 3):
            cnt += 1
        if (i % 5 == 0) and (i > 5):
            cnt += 1
        if (i % 7 == 0) and (i > 7):
            cnt += 1
        if cnt >= 1:
            answer+=1
            cnt = 0
    return answer