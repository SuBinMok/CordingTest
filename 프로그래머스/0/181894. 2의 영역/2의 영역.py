def solution(arr):
    answer = []
    a,b = -1, -1
    for i in range(len(arr)):
        if arr[i] == 2 and a == -1:
            a = i
    for k in range(len(arr)):
        i = len(arr) - k -1
        if arr[i] == 2 and b == -1:
            b = i
    if a == -1 or b == -1:
        answer =[-1]
    else:
        answer = arr[a:b+1]
    return answer