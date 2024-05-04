def solution(my_string):
    answer = []
    for i in my_string:
        if ord(i) < ord('A'):
            answer.append(int(i))
    return sorted(answer)