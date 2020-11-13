
def lcs(seq1, seq2):
    n, m = len(seq1) + 1, len(seq2) + 1
    dp = [[0] * m for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n - 1][m - 1]


def main():
    with open("lcs.in", "r") as fin, open("lcs.out", "w") as fout:
        N = fin.readline()
        seq1 = [i for i in fin.readline().split()]
        M = fin.readline()
        seq2 = [i for i in fin.readline().split()]

        fout.write(str(lcs(seq1, seq2)))


if __name__ == "__main__":
    main()
