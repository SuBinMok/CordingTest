from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for p in permutations(dungeons, len(dungeons)):
        total = 0
        left_power = k
        for i in range(len(p)):
            need_power = p[i][0]
            use_power = p[i][1]
            if left_power < need_power:
                break
            else:
                left_power -= use_power
                total += 1
        if answer < total:
            answer = total
    return answer