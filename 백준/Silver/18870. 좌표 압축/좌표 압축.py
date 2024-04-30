import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr)))
dic = {}
for idx, item in enumerate(arr2):
    dic[item] = idx 
    #arr2는 sorted 되어 있음, 따라서 item 보다 작은 숫자의 갯수는 idx가 됨.

for item in arr:
    print(dic[item], end=" ")