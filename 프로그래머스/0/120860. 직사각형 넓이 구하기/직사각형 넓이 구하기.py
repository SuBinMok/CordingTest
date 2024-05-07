def solution(dots):
    answer = 0
    x, y = 0, 0
    for i in range(1, 4):
        if abs(dots[0][0] - dots[i][0]) > x:
            x = abs(dots[0][0] - dots[i][0])
        if abs(dots[0][1] - dots[i][1]) > y:
            y = abs(dots[0][1] - dots[i][1])
    answer = x * y
    return answer