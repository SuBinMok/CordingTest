def solution(my_string):
    answer = ''
    m = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in m:
            answer+=i
    return answer