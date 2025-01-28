import sys


n = int(sys.stdin.readline())
meeting = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meeting.append([s,e])

meeting = sorted(meeting, key=lambda x: (x[1], x[0]))
count = 0
end = 0

for new_start, new_end in meeting:
    if end <= new_start:
        count+=1
        end = new_end
print(count)