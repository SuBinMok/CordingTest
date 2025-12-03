import sys

"""
ATM을 사용하기 위해 줄 서있는 사람들의 정렬을 어떤 기준으로 하여 최소 시간을 구하는 문제이다.
사용 시간이 가장 짧은 사람을 기준으로 정렬을 한 뒤에 대기시간을 구해 이 둘을 더한 값을 정답으로 return하면 된다.
"""

num = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
line.sort()
waiting_time = 0

for i in range(num):
    for j in range(i+1):
        waiting_time += line[j]

print(waiting_time)