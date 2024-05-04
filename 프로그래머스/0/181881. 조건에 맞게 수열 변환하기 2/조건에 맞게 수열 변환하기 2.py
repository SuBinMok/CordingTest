def solution(arr):
    answer = 0
    temp = [0] * len(arr)
    while True:
        if arr == temp:
            return answer-1
        else:
            temp = [k for k in arr]
            for i in range(len(arr)):
                if arr[i] >= 50 and arr[i] % 2 == 0:
                    arr[i] = arr[i]/2
                elif arr[i] < 50 and arr[i] % 2 != 0:
                    arr[i] = (arr[i]*2)+1
            answer += 1
solution([1, 2, 3, 100, 99, 98])