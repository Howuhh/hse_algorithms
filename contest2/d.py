from math import inf
from collections import deque

def argmin(arr):
    return min(enumerate(arr), key=lambda tup: tup[1])

def min_operations(n):
    dp = [inf] * (n + 1)
    prev = [-1] * (n + 1)
    
    dp[1] = 0
    for i in range(2, n + 1):
        div2 = i // 2 if i % 2 == 0 else 0
        div3 = i // 3 if i % 3 == 0 else 0
        sub1 = i - 1

        idx, numop = argmin([dp[div2], dp[div3], dp[sub1]])

        dp[i] = numop + 1
        prev[i] = [div2, div3, sub1][idx]

    last = n

    seq = deque([last])
    while last != -1:
        seq.appendleft(prev[last])
        last = prev[last]
    seq.popleft()

    return dp[n], seq



def main():
    with open("calcul.in", "r") as fin, open("calcul.out", "w") as fout:
        N = int(fin.readline())

        minop, seq = min_operations(N)
        fout.write(str(minop) + "\n")
        fout.write(" ".join([str(i) for i in seq]))

if __name__ == "__main__":
    main()