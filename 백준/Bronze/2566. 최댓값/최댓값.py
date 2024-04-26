arr = []
a, b = -1, -1
m = -1
for _ in range(9):
    s = input().split()
    arr.append(s)
for i in range(9):
    for j in range(9):
        if int(arr[i][j]) > m :
            m = int(arr[i][j])
            a, b = i, j
print(m)
print(a+1, b+1)