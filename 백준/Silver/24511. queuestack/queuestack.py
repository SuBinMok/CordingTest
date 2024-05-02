import sys
from collections import deque
n = int(sys.stdin.readline()) #수열 갯수
list_a = list(map(int, sys.stdin.readline().rstrip().split())) #0 : 큐, 1 : 스택
list_b = list(map(int, sys.stdin.readline().rstrip().split())) #삽입 당할
m = int(sys.stdin.readline()) #삽입할 수열 갯수
list_c = list(map(int, sys.stdin.readline().rstrip().split())) #삽입 할
x = 0
q = deque()
for i in range(n):
    if list_a[i] == 0:
        q.appendleft(list_b[i])

for j in range(m):
    q.append(list_c[j])
    print(q.popleft(), end= " ")