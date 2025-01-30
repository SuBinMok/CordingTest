import sys
n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr)

visited = [0]*n
result = []
def func():
    check = 0
    if len(result) == s:
        print(*result)
        return
    for i in range(n):
        if result and arr[i] < result[-1]:
            continue
        if check != arr[i]:

            visited[i] = True
            result.append(arr[i])
            check = arr[i]
            func()
            result.pop()
            visited[i] = False
func()