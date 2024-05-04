def solution(my_string):
    answer = 0
    temp = '0'
    for i in range(len(my_string)):
        if ord(my_string[i]) < ord('A'):
            temp += my_string[i]
        elif ord(my_string[i]) >= ord('A') and temp != '0':
            answer += int(temp)
            temp = '0'
    if temp != '0':
        answer+= int(temp)
    return answer