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



'''
문제를 풀면서 truck 큐만 사용해서 풀려고 했지만 1번 테케가 안풀려서 결국 다른 사람 답안을 참조해서 풀었음.
다리 길이 만큼 큐를 선언해서 그만큼 다리에 올려놓길 반복해서 풀기..
total은 다리 위에 놓인 트럭의 무게로 처음에 다리에서 내려가는 것부터 빼주고 
그 다음에 다리위로 들어오는 트럭의 무게가 weight보다 작으면 아래 코드를 실행.
만약 다리 위로 들어오는 트럭의 무게가 더 크면 다리 공간에 0을 추가해준다.
'''
