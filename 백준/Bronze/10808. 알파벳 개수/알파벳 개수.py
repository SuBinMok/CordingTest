s = input()
l = [0 for _ in range(26)]
for i in s:
    l[ord(i) - ord('a')] +=1

for i in l:
    print(i, end = ' ')