s = input()
result = 0
for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'B' or s[i] == 'C':
        result +=3
    elif s[i] == 'D' or s[i] == 'E' or s[i] == 'F':
        result +=4
    elif s[i] == 'G' or s[i] == 'H' or s[i] == 'I':
        result +=5
    elif s[i] == 'J' or s[i] == 'K' or s[i] == 'L':
        result +=6
    elif s[i] == 'M' or s[i] == 'N' or s[i] == 'O':
        result +=7
    elif s[i] == 'P' or s[i] == 'Q' or s[i] == 'R' or s[i] == 'S':
        result +=8
    elif s[i] == 'T' or s[i] == 'U' or s[i] == 'V':
        result +=9
    elif s[i] == 'W' or s[i] == 'X' or s[i] == 'Y'or s[i] == 'Z':
        result +=10
    else:
        result +=11
print(result)