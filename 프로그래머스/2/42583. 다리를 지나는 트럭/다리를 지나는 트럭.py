from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    total = 0
    while truck:
        time+=1
        total -= bridge.popleft()
        if total + truck[0] <= weight: #다리 위에 있는 트럭 무게가 weight보다 작거나 같은 겨웅
            w = truck.popleft() #truck 순서대로 pop함
            total += w #전체 무게에 더함
            bridge.append(w)#다리 위에 트럭 추가
        else: # 다리 위에 있는 트럭 무게가 weight보다 큰 경우
            bridge.append(0) #다리 위에 트럭을 추가 하지 않고 넘김
    return time + bridge_length