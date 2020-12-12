import sys
import math

def gcd(a, b):
    if b == 0:
        return a, 1, 0
    
    d, x1, y1 = gcd(b, a % b)
    
    x = y1
    y = x1 - y1 * (a // b)
    
    return d, x, y

def main():
    n, m = map(int, sys.stdin.readline().split())
    
    d, x, y = gcd(n, m)
    if d != 1:
        print(-1)
    else:
        print(x % m)


if __name__ == "__main__":
    main()