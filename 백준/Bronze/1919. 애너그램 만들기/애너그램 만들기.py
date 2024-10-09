s1 = str(input())
s2 = str(input())
l = [0 for _ in range(26)]
l1 = [0 for _ in range(26)]
l2 = [0 for _ in range(26)]
count = 0
for i in range(len(s1)):
    l1[ord(s1[i]) - ord('a')] += 1
for i in range(len(s2)):
    l2[ord(s2[i]) - ord('a')] += 1

for i in range(26):
    l[i] = l1[i] - l2[i]
for i in range(26):
    if l[i] != 0:
        count+= abs(l[i])
print(count)