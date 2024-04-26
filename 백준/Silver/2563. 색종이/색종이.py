buf = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
count = 0
for _ in range(n):
    w, h = map(int, input().split())
    for i in range(10):
        for j in range(10):
            buf[w + i - 1][h + j - 1] = 1

for x in range(100):
    for y in range(100):
        count += buf[x][y]
print(count)