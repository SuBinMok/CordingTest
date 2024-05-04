def solution(num, k):
    answer = -1
    num = str(num)
    for i in range(len(num)):
        if int(num[i]) == k:
            answer = i+1
            break
    return answer