def solution(n):
    answer = []
    for i in range(1, n+1):
        if i == n :
            answer.append(i)
            break
        if n % i == 0:
            answer.append(i)
    return sorted(answer)