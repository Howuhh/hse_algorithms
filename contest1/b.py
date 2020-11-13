import sys
from bisect import bisect_left, bisect_right

def main():
    n = int(sys.stdin.readline())
    arr = [(int(i), idx + 1) for idx, i in enumerate(sys.stdin.readline().split())]
    arr.sort()
   
    q = int(sys.stdin.readline())
    for _ in range(q):
        l, r, x = map(int, sys.stdin.readline().split())
        answ = False

        left, right = bisect_left(arr, (x, l)), bisect_right(arr, (x, r))

        if left < right:
            answ = True
    
        sys.stdout.write("1" if answ else "0")

if __name__ == "__main__":
    main()
