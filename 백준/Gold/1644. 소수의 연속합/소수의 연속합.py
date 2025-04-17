import sys

n = int(sys.stdin.readline())
l, r = 0, 0
answer = 0

def prime(m):
    p = 2
    is_prime = [True for _ in range(m + 1)]
    while (p*p <= m):
        if is_prime[p]:
            for i in range(p*p, m+1, p):
                is_prime[i] = False
        p+=1
    prime_numbers = [p for p in range(2, m+1) if is_prime[p]]
    return prime_numbers

prime_list = prime(n)
total = 0
k = len(prime_list)
while True:
    if total >= n:
        total -= prime_list[l]
        l+=1
    elif r==k:
        break
    else:
        total += prime_list[r]
        r+=1
    if total == n:
        answer+=1
print(answer)