def solution(n):
    a = 1
    for i in range(2, 11):
        if a*i > n:
            return i-1
        elif a*i != n:
            a= a*i
        elif a*i == n:
            return i
        
