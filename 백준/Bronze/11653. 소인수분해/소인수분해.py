N = int(input())
i = 2
for _ in range(N):
    if N > 1:
        if N % i == 0:
            N = N/i
            print(i)
        else :
            i += 1
    else:
      break