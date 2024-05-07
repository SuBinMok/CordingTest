def solution(my_string):
    answer = 0
    s = my_string.split()
    answer+= int(s[0])
    for i in range(len(s)):
        if s[i] == '+':
            answer += int(s[i+1])
        elif s[i] == '-':
            answer -= int(s[i+1])
    return answer