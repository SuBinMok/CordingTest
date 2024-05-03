def solution(strArr):
    arr = [len(i) for i in strArr]
    answer = []
    for i in set(arr) :
        answer.append(arr.count(i))
        
    return max(answer)