def solution(num, total):
    
    for i in range(-num, 1000):
        answer = []
        for j in range(num):
            answer.append(i+j)
        if sum(answer) == total:
            return answer