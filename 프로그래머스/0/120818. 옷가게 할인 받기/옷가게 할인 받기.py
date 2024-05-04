def solution(price):
    answer = 0
    if 300000 > price >= 100000:
        answer = price*0.95//1
    elif 500000 > price >= 300000:
        answer = price*0.9//1
    elif price >= 500000:
        answer = price*0.8//1
    else:
        answer = price
    return answer