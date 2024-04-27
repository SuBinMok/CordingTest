n = int(input())
x_list = []
y_list = []
for _ in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
if len(x_list) == 1:
    print(0)
else:
    xl = min(x_list)
    xr = max(x_list)
    yd = min(y_list)
    yu = max(y_list)
    print(abs(xr-xl)*abs(yu-yd))