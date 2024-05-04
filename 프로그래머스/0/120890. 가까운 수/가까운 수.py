def solution(array, n):
    answer = 0
    m = max(array)*9
    array = sorted(array)
    for i in array:
        if abs(n - i) < m:
            m = abs(n - i)
            answer = i
    return answer