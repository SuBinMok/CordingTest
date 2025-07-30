import sys

S, E, Q = map(str, sys.stdin.readline().split())
check = {}
S = int(S[:2] + S[3:])
E = int(E[:2] + E[3:])
Q = int(Q[:2] + Q[3:])
cnt = 0

while True:
    try:
        time, member = map(str, sys.stdin.readline().split())
        time =  int(time[:2] + time[3:])
        if time <= S:
            check[member] = 1
        elif E <= time <= Q:
            if check.get(member) and  check[member] == 1:
                cnt+=1
                check[member] = 0
    except:
        break

print(cnt)