def solution(quiz):
    answer = []
    for i in quiz:
        s = i.split()
        k = 0
        for sp in range(len(s)):
            if s[sp] == '=':
                r = s[sp+1:]
                if int(r[0]) == k:
                    answer.append("O")
                else:
                    answer.append("X")
                break
            elif s[sp] == '+':
                b = s[:sp]
                c = s[sp + 1:]
                k = int(b[0]) + int(c[0])
            elif s[sp] == '-':
                b = s[:sp]
                c = s[sp + 1:]
                k = int(b[0]) - int(c[0])
    return answer
