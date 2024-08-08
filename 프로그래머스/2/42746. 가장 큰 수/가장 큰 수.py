def solution(numbers):
    string_list = list(map(str, numbers))
    arr = sorted(string_list, key = lambda x: x*3, reverse = True)
    return str(int("".join(arr)))