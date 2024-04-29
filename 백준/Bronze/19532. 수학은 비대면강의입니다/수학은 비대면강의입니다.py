a, b, c, d, e, f = map(int, input().split())
r = c - f
x_ = a - d
y_ = b - e
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (c == a*x + b*y) and (f == d*x + e*y) :
            print(x, y)
            break