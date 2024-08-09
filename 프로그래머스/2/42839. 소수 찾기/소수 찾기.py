from itertools import permutations
def solution(numbers):
    answer = []
    num = [i for i in numbers]
    prime = []
    for i in range(1, len(num)+1):
        prime += list(permutations(num, i))
    prime =  [int(("").join(p)) for p in prime]
    
    for p in prime:
        check = True
        if p < 2 :
            continue
        for j in range(2, int(p**0.5)+1):
            if p % j == 0:
                check = False
                break
        if check:
            answer.append(p)            
    return len(set(answer))