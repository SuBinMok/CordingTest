arr = []
leng = []
res = ''
N = 5
for _ in range(N):
    i = input()
    arr.append(i)
    leng.append(len(i))
for i in range(max(leng)):
   for j in range(N):
      if i < leng[j]:
          res+=arr[j][i]
print(res)