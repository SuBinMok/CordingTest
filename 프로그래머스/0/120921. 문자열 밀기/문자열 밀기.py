def solution(A, B):
    answer = 0
    if A == B :
        return 0
    while True:
        if A == B:
            return answer
        else:
            A = A[-1] + A[:-1]
            answer +=1
        if answer == len(A):
            return -1
    return answer