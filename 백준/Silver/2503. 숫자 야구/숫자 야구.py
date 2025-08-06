import sys

N = int(sys.stdin.readline())
arr = []
number = []

def check(candidate, question, strike, ball):
    s = 0
    b = 0
    for i in range(3):
        if candidate[i] == int(question[i]):
            s += 1
        elif str(candidate[i]) in question:
            b += 1
    return s == strike and b == ball

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and i != k and j != k:
                n = int(str(i)+str(j)+str(k))
                number.append([i, j, k])
for i in range(N):
    num, strike, ball = map(int, sys.stdin.readline().split())
    n = list(str(num).strip())
    valid = []
    for c in number:
        if check(c, n, strike, ball):
            valid.append(c)
    number = valid

print(len(number))

