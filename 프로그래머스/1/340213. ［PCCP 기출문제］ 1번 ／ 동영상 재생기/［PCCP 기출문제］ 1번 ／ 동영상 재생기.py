def solution(video_len, pos, op_start, op_end, commands):
    #commands 는 next와 prev 밖에 없음.
    #시간이 오프닝 구간이면 자동 건너뛰기를 해준다.(기능 사용 전 후 상관 없이)
    answer = ''
    pos = int(pos[:2])*60+int(pos[-2:])
    op_start = int(op_start[:2])*60+int(op_start[-2:])
    op_end = int(op_end[:2])*60+int(op_end[-2:])
    video_len = int(video_len[:2])*60 + int(video_len[-2:])
    
    temp = pos
    
    for i in commands:
        if op_start <= temp <= op_end:
            temp = op_end
        if i == 'prev':   #10초 전
            if temp < 10:
                temp = 0
            else:
                temp -= 10            
        elif i == 'next': #10초 후
            if temp + 10 > video_len:
                temp = video_len
            else:
                temp += 10
        if op_start <= temp <= op_end:
            temp = op_end
    if temp//60 < 10:
        answer = '0'+str(temp//60)+':'
    else:
        answer = str(temp//60)+':'
    if temp % 60 < 10:
        answer += '0'+str(temp%60)
    else:
        answer += str(temp%60)
    
    return answer