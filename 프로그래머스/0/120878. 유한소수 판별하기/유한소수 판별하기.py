import math
def solution(a, b):
    answer = 0
    if a == b :
        return 1
    b = b // math.gcd(a, b)
    if b != 5 or b != 2 and b > 1:
        while True:
            if b % 5 == 0:
                b = b // 5
            elif b % 2 == 0:
                b = b // 2
            elif b % 2 != 0 and b % 5 != 0 or b == 1:
                break
    if b == 2 or b == 5 or b == 1:
        answer = 1
    else:
        answer = 2
    return answer