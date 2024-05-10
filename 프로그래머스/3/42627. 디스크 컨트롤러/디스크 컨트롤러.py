import heapq
def solution(jobs):
    l = []
    answer, n, cnt, now, start = 0, len(jobs), 0, 0, -1
    while cnt < n :
        for input_time, during_time in jobs:
            if start < input_time <= now:
                heapq.heappush(l, [during_time, input_time])
        if len(l) > 0:
            now_during, now_input = heapq.heappop(l)
            start = now
            now += now_during
            answer += (now - now_input)
            cnt += 1
        else:
            now += 1
    return int(answer // n)