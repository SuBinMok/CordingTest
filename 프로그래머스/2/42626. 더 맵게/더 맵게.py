#heapq이용 : 케이스 모두 통과 및 효율성 모두 통과
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



# 우선순위 큐 이용 : 케이스 모두 통과 및 효율성 2, 3, 5번 통과.
# 우선순위 큐가 heapq보다 더 느린듯.. 
# from queue import PriorityQueue
# def solution(scoville, K):
#     q = PriorityQueue(len(scoville))
#     for i in scoville:
#         q.put(i)
#     answer = 0
#     while not q.empty():
#         first = q.get()
#         size = q.qsize()
#         if size == 0 and first < K:
#             return -1
#         elif size != 0 and first < K:
#             second = q.get()
#             q.put(first + (second*2))
#             answer += 1
#         elif first >= K:
#             break
#     return answer
