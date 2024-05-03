def solution(order):
    answer = 0
    menu = ["americano", "cafelatte"]
    for i in order:
        if i[3:] == menu[0] or i[:-3] == menu[0] or i == menu[0]:
            answer += 4500
        elif i[3:] == menu[1] or i[:-3] == menu[1] or i == menu[1]:
            answer += 5000
        else:
            answer+= 4500
    return answer