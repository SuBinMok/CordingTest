import sys

n, won = map(int, sys.stdin.readline().split())
coins = []
need = 0
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

coins = list(reversed(coins))
while won > 0:
    for i in coins:
        if i <= won:
            wons = won // i
            if wons > 0:
                won = won - (wons*i)
                need += wons
print(need)