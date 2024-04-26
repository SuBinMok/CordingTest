while True:
    num = int(input())
    if num == -1:
      break
    l = []
    r = 0
    for i in range(1, num):
        if num % i == 0:
            l.append(i)
            r += i
    if r == num:
        k = len(l)-1
        print(f"{num} = ", end = '')
        for i in range(len(l)):
            print(f"{l[i]}", end = '')
            if k != 0:
                print(" + ", end = '')
                k -= 1
    else:
        print(f"{num} is NOT perfect.", end='')
    print("")