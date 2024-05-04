def solution(my_string):
    answer = ''
    temp = sorted(my_string.lower())
    for i in temp:
        answer+=i
    return answer