def solution(arr, k):
    answer = []
    arr2 = []
    for i in range(len(arr)):
        if len(arr2) == 0:
            arr2.append(arr[i])
        elif arr[i] not in arr2:
            arr2.append(arr[i])
    for i in range(k):
        if i < len(arr2):
            answer.append(arr2[i])
        else:
            answer.append(-1)
    return answer
print(solution([0, 3, 2, 3, 1], 5))