def solution(wallet, bill):
    #긴쪽을 접는다.
    #접어서 들어가면 그대로 넣는다.
    #안들어가면 90도 회전한다.
    #그래도 안들어가면 또 접는다.
    answer = 0
    if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
        return 0
    else:
        while True:
            if bill[0] >= bill[1]:
                bill[0] = bill[0] // 2
            elif bill[1] > bill[0]:
                bill[1] = bill[1] // 2
            answer +=1
            if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
                break
            else:
                temp = bill[0]
                bill[0] = bill[1]
                bill[1] = temp
            if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
                break
            else:
                temp = bill[0]
                bill[0] = bill[1]
                bill[1] = temp
    return answer