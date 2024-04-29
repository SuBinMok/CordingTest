n, limit_num = map(int, input().split())
n_list = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and i != k and j != k and result <= n_list[i]+n_list[j]+n_list[k] <= limit_num:
                result = n_list[i]+n_list[j]+n_list[k]
print(result)