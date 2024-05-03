def solution(myString, pat):
    answer = ''
    temp = 0
    for i in range(len(myString)):
        if myString[i:i+len(pat)] == pat:
            temp = i + len(pat)
    answer = myString[:temp]
    return answer