n = int(input())
l = list(map(int, input().split()))
v = int(input())
nl = [0] * 201

for i in l:
    nl[i] += 1

print(nl[v])

