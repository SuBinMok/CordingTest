def solution(arr):
    answer = arr.copy()
    x = len(arr)
    y = len(arr[0])
    add = 0
    if x < y:
        add = y - x
        ar = [0 for _ in range(y)]
        for _ in range(add):
            answer.append(ar)
    elif x > y:
        add = x - y
        for _ in range(add):
            for i in range(x):
                answer[i].append(0)
    return answer