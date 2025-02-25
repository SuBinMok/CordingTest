import sys

pick, app = map(int, sys.stdin.readline().split())
dic = {}

for i in range(app):
    number = sys.stdin.readline().strip()
    dic[number] = i
safe = sorted(dic.items(), key=lambda x:x[1])
if pick > len(safe):
    pick = len(safe)
for i in range(pick):
    print(safe[i][0])