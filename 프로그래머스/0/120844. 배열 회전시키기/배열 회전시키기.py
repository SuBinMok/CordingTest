def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers[-1])
        for i in range(0, len(numbers)-1):
            answer.append(numbers[i])
    elif direction == "left":
        for i in range(1, len(numbers)):
            answer.append(numbers[i])
        answer.append(numbers[0])
    return answer