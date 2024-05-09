import heapq
def solution(scoville, K):
    heapq.heapify(scoville) # 리스트 scoville을 heapq로 대체하는 것
    answer = 0
    if scoville[0] >= K:
        return 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first+second*2)
        answer+=1
    return answer