def solution(dots):
    answer = 0
    l = []
    #(y2-y1)/(x2-x1)가 같은 것을 찾으면 됨
    for i in range(1, len(dots), 2):
        l.append([dots[(i-1)][0], dots[(i-1)][1], dots[i][0], dots[i][1], (dots[i][1]-dots[(i-1)][1])/(dots[i][0]-dots[(i-1)][0])])
    l.append([dots[0][0], dots[0][1], dots[2][0], dots[2][1], (dots[2][1]-dots[0][1])/(dots[2][0]-dots[0][0])])
    l.append([dots[1][0], dots[1][1], dots[3][0], dots[3][1], (dots[3][1]-dots[1][1])/(dots[3][0]-dots[1][0])])
    print(l)
    for i in range(len(l)):
        con = l[i][4]
        for j in range(len(l)):
            if i != j and con == l[j][4]:
                if (l[i][0] != l[j][0] and l[i][1] != l[j][1]) and (l[i][2] != l[j][2] and l[i][3] != l[j][3]) and (l[i][0] != l[j][2] and l[i][1] != l[j][3]) and (l[i][2] != l[j][0] and l[i][3] != l[j][1]):
                    answer=1
    return answer