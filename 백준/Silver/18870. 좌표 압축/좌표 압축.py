import sys


n = int(sys.stdin.readline())
a_list = list(map(int, sys.stdin.readline().split()))
sort_a = sorted(list(set(a_list)))
dic = {sort_a[i]: i for i in range(len(sort_a))}

for i in a_list:
    print(dic[i], end= ' ')