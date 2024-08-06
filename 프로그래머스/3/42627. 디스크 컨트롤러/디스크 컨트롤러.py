import heapq
def solution(jobs):
    answer, n, now, start = 0, len(jobs), 0, -1
    work = []
    while n != 0:
        for into, during in jobs:
            if start < into <= now:
                heapq.heappush(work, [during, into])
        if len(work) > 0:
            during, into = heapq.heappop(work)
            start = now
            now += during
            answer += (now - into)
            n -= 1
        else:
            now +=1  
    return int(answer // len(jobs))