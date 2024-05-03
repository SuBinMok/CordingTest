def solution(myString, pat):
    answer = 0
    p = len(pat)
    for i in range(len(myString)):
        if myString[i:i+p] == pat:
            answer+=1
    return answer