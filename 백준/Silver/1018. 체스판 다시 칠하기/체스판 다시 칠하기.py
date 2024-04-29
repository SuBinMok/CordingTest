row, colmn = map(int, input().split())
map_list = [input() for _ in range(row)]
result = []
for r in range(row - 7):
    for c in range(colmn - 7):
        cntb, cntw = 0, 0
        for i in range(r, r+8):
            for j in range(c, c+8):
                if (i+j)%2 == 0:
                    if map_list[i][j] != 'B':
                        cntb+=1
                    elif map_list[i][j] != 'W':
                        cntw+=1
                if (i+j)%2 != 0:
                      if map_list[i][j] != 'W':
                          cntb+=1
                      elif map_list[i][j] != 'B':
                          cntw+=1
        result.append(cntw)
        result.append(cntb)
print(min(result))