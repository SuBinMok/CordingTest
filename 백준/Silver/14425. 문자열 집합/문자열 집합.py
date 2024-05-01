import sys
input = sys.stdin.readline
list_n, test_n = map(int, input().split())
cnt = 0
l = ['']*list_n
t = ['']*test_n
for i in range(list_n):
    l[i] = input()
for i in range(test_n):
    t[i] = input()

dic = {}
for i in range(list_n):
    dic[l[i]] = 0
for i in t:
    if i not in dic:
        continue
    else:
        cnt+=1
print(cnt)