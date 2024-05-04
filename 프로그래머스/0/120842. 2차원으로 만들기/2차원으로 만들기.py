def solution(num_list, n):
    answer = [[0]*n for _ in range(len(num_list)//n)]
    for i in range(len(num_list)//n):
        for j in range(n):
            answer[i][j] = num_list[(i*n)+j]
    return answer