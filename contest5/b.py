import sys

def z_function(s):
    z = [0] * len(s)
    
    l, r = 0, 0
    for i in range(1, len(s)):
        k = max(min(z[i - l], r - i), 0)
        
        while i + k < len(s) and s[k] == s[i + k]:
            k += 1
        z[i] = k
        
        if i + z[i] > r:
            l, r  = i, i + z[i]    
    return z


def main():
    n, m = map(int, sys.stdin.readline().split())
    cubes = [int(i) for i in sys.stdin.readline().split()]
    
    all_cubes = [-1] * (2 * n + 1)
    
    for i in range(n):
        all_cubes[i] = cubes[i]
        all_cubes[2 * n - i] = cubes[i]
    
    z = z_function(all_cubes)

    for i in range(n + 1, len(all_cubes)):
        if z[i] == len(all_cubes) - i and z[i] % 2 == 0:
            print(n  - z[i] // 2)
    print(n)
    
    
if __name__ == "__main__":
    main()