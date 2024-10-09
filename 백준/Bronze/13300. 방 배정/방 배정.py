n, r = map(int, input().split())
l = [[0, 0] for _ in range(6)]

girl = 0
boy = 0
for _ in range(n):
    sex, grade = map(int, input().split())
    l[grade-1][sex]+=1
for i in range(6):
    girl += int((l[i][0]+1)/2)
    boy += int((l[i][1]+1)/2)
print(girl + boy)