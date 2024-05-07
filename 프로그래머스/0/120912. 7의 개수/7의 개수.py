def solution(array):
    answer = 0
    a = [str(i) for i in array]
    for k in a:
        for j in k:
            if j == '7':
                answer+=1
    return answer