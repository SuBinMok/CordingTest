kg = int(input())
com = [kg, kg, kg]
f, t, ft = 0, 0, 0
if kg % 5 == 0:
    com[0] = kg // 5
    f = 1
if kg % 3 == 0:
    com[1] = kg // 3
    t = 1
for i in range(kg//5+1):
    for j in range(kg//3+1):
        if kg == 5*i + 3*j:
            com[2] = i+j
            ft = 1
if f == 1 or t == 1 or ft == 1:
    print(min(com))
else:
    print(-1)