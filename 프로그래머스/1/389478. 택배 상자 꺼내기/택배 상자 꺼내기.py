def solution(n, w, num):
    answer = 0
    h = n//w +1
    x = 1
    storage = []
    for i in range(h):
        temp = []
        for j in range(w):
            if x <= n:
                temp.append(x)
                x+=1
            else:
                temp.append(0)
        if i % 2 == 0:
            storage.append(temp)
        else:
            temp.reverse()
            storage.append(temp)
    
    for i in range(h):
        for j in range(w):
            if storage[i][j] == num:
                d = i
                while d < h and storage[d][j]:
                    answer +=1
                    d+=1
    return answer