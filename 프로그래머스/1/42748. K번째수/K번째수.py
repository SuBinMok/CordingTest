def solution(array, commands):
    answer = []
    for i, j, k in commands:
        arr = []
        arr = array[i-1:j]
        arr = sorted(arr)
        answer.append(arr[k-1])
    return answer