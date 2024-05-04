def solution(n):
    answer = []
    for i in range(1, n+1):
        if i * (n//i) == n:
            answer.append([i, n//i])
    return len(answer)