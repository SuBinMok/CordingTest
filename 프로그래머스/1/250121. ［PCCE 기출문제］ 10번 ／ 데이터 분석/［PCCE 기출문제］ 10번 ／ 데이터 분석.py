def solution(data, ext, val_ext, sort_by):
    answer = []
    for i in range(len(data)):
        if ext == 'date':
            if data[i][1] <= val_ext:
                answer.append(data[i])
        elif ext == 'code':
            if data[i][0] <= val_ext:
                answer.append(data[i])
        elif ext == 'maximum':
            if data[i][2] <= val_ext:
                answer.append(data[i])
        elif ext == 'remain':
            if data[i][3] <= val_ext:
                answer.append(data[i])
    if sort_by == 'remain':
        answer.sort(key = lambda x: x[3])
    elif sort_by == 'maximum':
        answer.sort(key = lambda x: x[2])
    elif sort_by == 'code':
        answer.sort(key = lambda x: x[0])
    elif sort_by == 'date':
        answer.sort(key = lambda x: x[1])
    return answer