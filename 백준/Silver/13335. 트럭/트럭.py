import sys
from collections import deque
n, w, l = map(int, sys.stdin.readline().split())# 트럭 수, 다리 길이, 최대 하중
truck = deque(map(int, sys.stdin.readline().split()))

weight = 0 # 다리 위에 올라간 트럭 무게
cnt = 0 # 다리 위에 올라간 트럭 갯수
time = 0 # 트럭이 모두 다리를 건넌 시간
bridge = deque([0]*w)

while weight > 0 or truck:
    time += 1
    exist_truck = bridge.popleft()
    weight -= exist_truck

    if truck:
        new_truck_weight = truck[0]
        if weight + new_truck_weight <= l:
            t = truck.popleft()
            bridge.append(t)
            weight += t
        else:
            bridge.append(0)
    else:
        bridge.append(0)

print(time)