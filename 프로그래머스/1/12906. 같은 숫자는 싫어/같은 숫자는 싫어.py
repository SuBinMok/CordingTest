def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] and i == len(arr)-2:
            answer.append(arr[i])
        elif arr[i] != arr[i+1] and i == len(arr)-2:
            answer.append(arr[i])
            answer.append(arr[i+1])
            break
        elif arr[i] != arr[i+1]:
            answer.append(arr[i])
        
    return answer