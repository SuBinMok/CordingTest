import sys
from collections import deque
n, m, k = map(int, sys.stdin.readline().split())
sticker = []
laptop = [[0]*m for _ in range(n)]
answer = 0
for _ in range(k):
    sn, sm = map(int, sys.stdin.readline().split())
    s = []
    for _ in range(sn):
        s.append(list(map(int, sys.stdin.readline().split())))
    sticker.append(s)

# rotation() : 스티커 회전 , 최대 4번까지만.
def rotation(arr):
    rot_arr = zip(*arr[::-1])
    return [list(l) for l in rot_arr]

def search(x, y, st):
    for i in range(len(st)):
        for j in range(len(st[0])):
            if st[i][j] == 0:
                continue
            nx = x+i
            ny = y+j
            if not(0 <= nx < n and 0 <= ny < m):
                return False
            if laptop[nx][ny] == 1:
                return False
    return True

def att(x, y, st):
    for i in range(len(st)):
        for j in range(len(st[0])):
            if st[i][j] == 0:
                continue
            nx = x + i
            ny = y + j
            laptop[nx][ny] = 1

def main(s):
    for rot in range(4):
        for x in range(n):
            for y in range(m):
                put_sticker = search(x, y, s)
                if put_sticker:
                    att(x, y, s)
                    return
        s = rotation(s)

while sticker:
    s = sticker.pop(0)
    main(s)
for i in range(n):
    answer+= laptop[i].count(1)
print(answer)