import sys
import math

cr = int(sys.stdin.readline())
student = list(map(int, sys.stdin.readline().rstrip().split()))
sup, sub = map(int, sys.stdin.readline().rstrip().split())
answer = 0
for i in range(cr):
    answer += 1

    student[i] -= sup
    if student[i] > 0:
        answer += math.ceil(student[i]/sub)

print(answer)