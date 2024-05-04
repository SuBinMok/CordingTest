def solution(my_string):
    answer = ''
    for i in my_string:
        if ord('A') <= ord(i) <= ord('Z'):
            answer+= i.lower()
        elif ord('a') <= ord(i) <= ord('z'):
            answer+= i.upper()
    return answer