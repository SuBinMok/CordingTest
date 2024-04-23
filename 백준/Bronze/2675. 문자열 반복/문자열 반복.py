repeat = int(input())
for _ in range(repeat):
    n, s = input().split()
    for i in range(len(s)):
        print(s[i]*int(n), end ="")
    print()    