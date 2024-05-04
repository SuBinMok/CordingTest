def solution(numer1, denom1, numer2, denom2):
    N = numer1 * denom2 + numer2 * denom1
    D = denom1 * denom2
    return [N//gcd(N,D), D//gcd(N,D)]

def gcd(a,b):
    while b:
        a,b = b, a % b
    return a