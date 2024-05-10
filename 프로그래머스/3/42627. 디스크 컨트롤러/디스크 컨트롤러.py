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


# 아래 코드는 70 / 100 , 하다가 하다가 안되서 결국 질문 게시판 참고해서 함.. 문제 이해 자체를 제대로 못한거같음. 다음에 다시 풀어보기
# import heapq
# def solution(jobs):
#     jobs.sort(key=lambda x: x[0])
#     n = len(jobs)
#     l = []
#     heapq.heapify(l)
#     heapq.heapify(jobs)
#     s, d = heapq.heappop(jobs)
#     end = s + d # 실행 종료 시점
#     prosess_time = d # 전체 프로세스에 걸린 시간
#     for i in range(len(jobs)): #현재 시점에서 가장 빨리 끝날 수 있는 것 찾기
#         s, d = heapq.heappop(jobs)
#         if end - s >= 0: # 현재 실행 시점에 들어온 것
#             heapq.heappush(l, [end + d, s, d]) #끝나는 시간, 입력된 시간, 걸리는 시간
#         else:
#             heapq.heappush(l, [s+d, s, d])
#     while len(l) > 0:
#         e, s, d = heapq.heappop(l) #실행 종료 시점, 입력 시점, 걸리는 시간
#         if e - s >= 0: #실행 중 들어온 것.
#             prosess_time += e - s
#         else: #실행 모두 끝난 후 들어온 것
#             prosess_time += d  # 전체 프로세스에 걸린 시간
#         for i in range(len(l)):
#             _, s, d = heapq.heappop(l)
#             heapq.heappush(l, [e+d, s, d])
#     return int(prosess_time / n)
