def solution(babbling):
    answer = 0
    bab = ["aya", "ye", "woo", "ma"]
    combi = []
    for i in range(len(bab)+1, 0, -1):
        temp = perm(bab, i)
        # print(temp)
        for j in range(len(temp)):
            t = ''
            for a in range(len(temp[j])):
                t += temp[j][a]
            combi.append(t)
    for i in babbling:
        if i in combi:
            answer+=1
    return answer

def perm(arr, n):
    res = []
    if n == 0:
        return [[]]
    for i in range(0, len(arr)): 
        elem = arr[i]   
        for P in perm(arr[:i] + arr[i + 1:], n-1): 
            res.append([elem]+P) 
              
    return res
