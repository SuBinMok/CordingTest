n, c = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
print(lst[-c])