def solution(arr):
    answer = [i for i in arr]
    z = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    app = 0
    for i in z:
        if i >= len(arr):
            app = i - len(arr)
            break
    for _ in range(app):
        answer.append(0)
    return answer