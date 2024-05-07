def solution(my_str, n):
    answer = []
    if len(my_str)%n != 0:
        for i in range(len(my_str)//n+1):
            answer.append(my_str[i*n:(i+1)*n])
    else:
        for i in range(len(my_str)//n):
            answer.append(my_str[i*n:(i+1)*n])
        
    return answer