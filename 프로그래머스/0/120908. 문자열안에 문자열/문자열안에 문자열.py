def solution(str1, str2):
    answer = 0
    if len(str1) == len(str2) and str1 == str2:
        answer = 1
    else:
        for i in range(len(str1)-len(str2)+1):
            if str1[i:i+len(str2)] == str2:
                answer=1
    if answer == 0:
        answer = 2
    return answer