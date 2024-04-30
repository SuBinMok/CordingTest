import sys
input = sys.stdin.readline
s_n = int(input())
s_l = list(map(int, input().split()))
w_n = int(input())
w_l = list(map(int, input().split()))
dic = {}

for i in range(s_n):
    dic[s_l[i]] = 0
for i in w_l:
    if i not in dic:
        print(0, end=' ')
    else:
        print(1, end=" ")