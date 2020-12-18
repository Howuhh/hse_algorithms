import sys

def prefix_function(s):
    p = [0] * len(s)
    
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[i] != s[k]:
            k = p[k - 1]
        if s[i] == s[k]:
            k = k + 1
        p[i] = k
    return p
        
def main():
    S = sys.stdin.readline().strip()
    print(len(S) - prefix_function(S)[-1])
    

if __name__ == "__main__":
    main()