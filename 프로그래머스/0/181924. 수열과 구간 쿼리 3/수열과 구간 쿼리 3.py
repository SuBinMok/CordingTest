def solution(arr, queries):
    answer = [i for i in arr]
    for i, j in queries:
        a = answer[i]
        answer[i] = answer[j]
        answer[j] = a
    return answer