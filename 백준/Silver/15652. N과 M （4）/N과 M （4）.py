import sys
n, s = map(int, sys.stdin.readline().split())
visited = [0]*n
result = []

def func():
    if len(result) == s:
        print(*result)
        return
    for i in range(n):
        if result and i+2 <= result[-1]:
            continue
        visited[i] = True
        result.append(i+1)
        func()
        visited[i] = False
        result.pop()

func()