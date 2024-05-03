def solution(myString):
    answer = []
    return sorted(i for i in myString.split('x') if i)