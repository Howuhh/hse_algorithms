import sys
import math

def gcd(a, b):
    if b == 0:
        return a, 1, 0
    
    d, x1, y1 = gcd(b, a % b)
    
    x = y1
    y = x1 - y1 * (a // b)
    
    return d, x, y

def modulo_inverse(n, m):
    d, x, y = gcd(n, m)
    if d != 1:
        return
    return x % m

def prime_factorization(n):
    primes = set()
    
    p = 2
    while p * p <= n:
        while n % p == 0:
            n = n / p
            primes.add(p)
        p = p + 1
    
    if n > 1:
        primes.add(n) 
    
    return primes

def euler_function(n):
    primes = prime_factorization(n)

    phi = n
    for p in primes:
        phi = phi * (1 - 1/p)
    
    return int(phi)


def main():
    n = int(input())
    e = int(input())
    C = int(input())

    phi_n = euler_function(n)
    d = modulo_inverse(e, phi_n)
    
    M = pow(C, d, n)
    print(M)

if __name__ == "__main__":
    main()