def solution(numbers):
    answer = ''
    s = list(map(str, numbers))
    arr = sorted(s, key = lambda x: x*3, reverse = True)
    return str(int("".join(arr)))