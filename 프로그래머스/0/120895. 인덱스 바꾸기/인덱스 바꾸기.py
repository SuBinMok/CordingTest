def solution(my_string, num1, num2):
    answer = ''
    my_string = list(my_string)
    temp1 = my_string[num1]
    temp2 = my_string[num2]
    my_string[num1] = temp2
    my_string[num2] = temp1
    for i in my_string:
        answer+= i
    return answer