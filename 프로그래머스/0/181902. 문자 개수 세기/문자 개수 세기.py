def solution(my_string):
    answer = [0]*52
    for i in my_string:
        if ord(i) < ord('a'):
            answer[ord(i)-ord('A')] +=1
        else:
            answer[ord(i)-ord('A')-6] +=1
    return answer