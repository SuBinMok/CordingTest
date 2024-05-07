def solution(balls, share):
    answer = 0
    a, b, c = 1, 1, 1 #각각 n!, m!, (n-m)!
    check = 0
    for i in range(balls, 0, -1):
        a = a * i
    for i in range(share, 0, -1):
        b = b * i
    for i in range(balls-share, 0, -1):
        c = c * i
        
    answer = a /(b*c)
    return answer