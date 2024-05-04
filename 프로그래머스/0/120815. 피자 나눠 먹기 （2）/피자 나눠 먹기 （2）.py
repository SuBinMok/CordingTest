def solution(n):
    i = 0
    while True:
        i += 1
        if (n*i)%6 == 0:
            break
    return i*n/6