from collections import deque
def solution(prices):
    answer = []
    price = deque(prices)
    while price:
        p = price.popleft()
        change = 0
        for i in price:
            if p <= i :
                change +=1
            else:
                change +=1
                break
        answer.append(change)
    return answer