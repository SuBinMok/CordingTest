n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    a_list = [0 for _ in range(26)]
    b_list = [0 for _ in range(26)]
    for i in a:
        a_list[ord(i)-ord('a')] += 1
    for i in b:
        b_list[ord(i)-ord('a')] += 1
    if a_list == b_list:
        print("Possible")
    else:
        print("Impossible")