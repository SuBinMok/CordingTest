n = int(input())
result = 0

for i in range(n):
    temp = str(i)
    t = 0
    for j in range(len(temp)):
        t += int(temp[j])
    if i + t == n:
        result = i
        break
print(result)
        