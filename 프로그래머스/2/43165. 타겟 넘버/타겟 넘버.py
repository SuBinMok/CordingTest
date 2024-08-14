def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        temp = []
        for leaf in leaves:
            temp.append(leaf+num)
            temp.append(leaf-num)
        leaves = temp
    for leaf in leaves:
        if leaf == target:
            answer+=1
    return answer