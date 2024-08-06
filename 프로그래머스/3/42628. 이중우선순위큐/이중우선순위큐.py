import heapq
def solution(operations):
    answer = []
    h = []
    for i in operations:
        a, b = i.split()
        b = int(b)
        if a == "I":
            heapq.heappush(h, b)
        else:    
            if h:
                if b == 1:
                    h.sort()
                    h.pop()
                else:
                    heapq.heappop(h)
    h.sort()
    if h:
        answer = [h[-1], h[0]]
    else:
        answer = [0, 0]
    return answer