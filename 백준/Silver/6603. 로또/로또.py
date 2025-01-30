import sys


def func(index):

    if len(res) == 6:
        print(*res)
        return
    for i in range(index, len(arr)):
        if res and arr[i] == res[-1]:
            continue
        if not visited[i]:
            res.append(arr[i])
            func(i + 1)
            res.pop()
while True:
    arr = list(map(int, sys.stdin.readline().strip().split()))
    k = arr[0]
    arr= arr[1:]
    res = []
    visited = [0] * (len(arr))
    if k == 0:
        break
    func(0)
    print()