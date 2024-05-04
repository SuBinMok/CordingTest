def solution(numbers):
    answer = 0
    numbers = sorted(numbers, reverse = True)
    answer = numbers[0] * numbers[1]
    return answer