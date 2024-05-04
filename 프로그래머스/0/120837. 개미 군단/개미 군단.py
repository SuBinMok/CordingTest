def solution(hp):
    answer = 0
    ant = [5, 3, 1]
    for i in ant:
        if hp > 0:
            answer += hp//i
            hp = hp - i*(hp//i)           
    return answer