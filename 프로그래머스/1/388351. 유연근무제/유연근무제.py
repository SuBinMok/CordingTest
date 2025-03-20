def solution(schedules, timelogs, startday):
    answer = 0
    accept = [i + 10 if i%100<50 else i+50 for i in schedules]
    log = [[0 for i in range(len(timelogs[0]))] for i in range(len(timelogs))]

    for i in range(len(timelogs)):
        day = startday
        for j in range(len(timelogs[0])):
            if day > 5:
                log[i][j] = 1
            elif day <= 5:
                if timelogs[i][j] <= accept[i]:
                    log[i][j] = 1
            if day == 7:
                day = 0
            day +=1

    for i in range(len(log)):
        sum = 0
        for j in range(len(log[0])):
            if log[i][j] == 1:
                sum+=1
        if sum == 7:
            answer +=1
    return answer