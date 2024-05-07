def solution(numbers, k):
    answer = 0
    while k > 1:
        k-=1
        remove = numbers.pop(0)
        numbers.append(remove)
        remove = numbers.pop(0)
        numbers.append(remove)
    answer = numbers.pop(0)
    return answer