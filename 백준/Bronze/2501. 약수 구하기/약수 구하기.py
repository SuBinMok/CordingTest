n, number = map(int, input().split())
l = []
for i in range(1, n+1):
    if n%i == 0:
        l.append(i)
if len(l) < number:
    print(0) 
else:
    print(l[number-1])