import sys
input = sys.stdin.readline
n = int(input())
s_list = list(map(int, input().split()))
t = int(input())
t_list = list(map(int, input().split()))
s_dic = {}
for i in s_list:
    if i not in s_dic:
        s_dic[i] = 0
    s_dic[i] += 1
for i in t_list:
    if i not in s_dic:
        print("0", end=" ")
    else:
        print(s_dic[i], end=" ")