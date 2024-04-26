def solution(arr, queries):
    answer = []
    for i, j in queries:
        for a in range(i, j+1):
            arr[a] +=1
    return arr