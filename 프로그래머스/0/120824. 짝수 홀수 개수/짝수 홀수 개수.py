def solution(num_list):
    o = 0 #홀수
    c = 0 #짝수
    for i in num_list:
        if i % 2 == 0:
            c += 1
        else:
            o += 1
            
    return [c, o]