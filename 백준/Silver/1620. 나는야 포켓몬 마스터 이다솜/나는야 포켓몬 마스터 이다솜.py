import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pocket_dic = {}
for i in range(n):
    pocket = input().rstrip()
    pocket_dic[str(i+1)] = pocket #key : i, item : pocket_name
    pocket_dic[pocket] = str(i+1)

for _ in range(m):
    print(pocket_dic[str(input()).rstrip()])