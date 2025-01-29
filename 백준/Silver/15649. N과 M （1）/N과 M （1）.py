import sys
n, m = map(int, sys.stdin.readline().split())
visited = [0]*n
arr = [0]*n
def func(k):
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    for i in range(n):
        if not visited[i]:
            arr[k] = i+1
            visited[i]=1
            func(k+1)
            visited[i] = 0

func(0)