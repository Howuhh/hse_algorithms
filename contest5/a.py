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
    s = sys.stdin.readline().strip() * 2 
    z = z_function(s)

    pos = 1
    for i in range(len(s) // 2):
        if i + z[i] < len(s) and s[z[i]] > s[i + z[i]]:
            pos = pos + 1
            
    print(pos)
    

if __name__ == "__main__":
    main()