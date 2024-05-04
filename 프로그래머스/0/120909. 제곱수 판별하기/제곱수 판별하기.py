def solution(n):
    answer = 0
    if n**(1/2) % 1 == 0:
        answer = 1
    else:
        answer = 2
    return answer