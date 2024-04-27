x, y, w, h = map(int, input().split())
min_x, min_y = x, y
mini = 0
if min_x > w - x:
    min_x = w - x
if min_y > h - y:
    min_y = h - y
if min_x >= min_y:
    mini = min_y
elif min_x < min_y:
    mini = min_x
print(mini)