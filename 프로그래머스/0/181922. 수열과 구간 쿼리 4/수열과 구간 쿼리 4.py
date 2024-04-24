def solution(arr, queries):
    answer = [arr[i] for i in range(len(arr))]
    for s, e, k in queries:
        for i in range(s, e+1):
            if i % k == 0:
                answer[i] += 1
    return answer