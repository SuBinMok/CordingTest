def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
    w_max = max(sizes, key = lambda x : x[0])
    h_max = max(sizes, key = lambda x : x[1])
    return w_max[0]*h_max[1]