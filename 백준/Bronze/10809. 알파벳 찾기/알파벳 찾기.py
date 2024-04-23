s = str(input())
result = [-1] * 26
for i in range(len(s)):
    if s[i] == 'a' and result[0] == -1:
        result[0] = i
    elif s[i] == 'b' and result[1] == -1:
        result[1] = i
    elif s[i] == 'c' and result[2] == -1:
        result[2] = i
    elif s[i] == 'd' and result[3] == -1:
        result[3] = i
    elif s[i] == 'e' and result[4] == -1:
        result[4] = i
    elif s[i] == 'f' and result[5] == -1:
        result[5] = i
    elif s[i] == 'g' and result[6] == -1:
        result[6] = i
    elif s[i] == 'h' and result[7] == -1:
        result[7] = i
    elif s[i] == 'i' and result[8] == -1:
        result[8] = i
    elif s[i] == 'j' and result[9] == -1:
        result[9] = i
    elif s[i] == 'k' and result[10] == -1:
        result[10] = i
    elif s[i] == 'l' and result[11] == -1:
        result[11] = i
    elif s[i] == 'm' and result[12] == -1:
        result[12] = i
    elif s[i] == 'n' and result[13] == -1:
        result[13] = i
    elif s[i] == 'o' and result[14] == -1:
        result[14] = i
    elif s[i] == 'p' and result[15] == -1:
        result[15] = i
    elif s[i] == 'q' and result[16] == -1:
        result[16] = i
    elif s[i] == 'r' and result[17] == -1:
        result[17] = i
    elif s[i] == 's' and result[18] == -1:
        result[18] = i
    elif s[i] == 't' and result[19] == -1:
        result[19] = i
    elif s[i] == 'u' and result[20] == -1:
        result[20] = i
    elif s[i] == 'v' and result[21] == -1:
        result[21] = i
    elif s[i] == 'w' and result[22] == -1:
        result[22] = i
    elif s[i] == 'x' and result[23] == -1:
        result[23] = i
    elif s[i] == 'y' and result[24] == -1:
        result[24] = i
    elif s[i] == 'z' and result[25] == -1:
        result[25] = i
for i in range(26)    :
    print(result[i], end= " ")