def cost(a, b):
    return 1 if a != b else 0

def levenshtein_dist(seq1, seq2):
    n, m = len(seq1) + 1, len(seq2) + 1

    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        dp[i][0] = i

    for i in range(m):
        dp[0][i] = i

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # insert
                dp[i][j - 1] + 1,  # delete
                dp[i - 1][j - 1] + cost(seq1[i - 1], seq2[j - 1])  # subst
            )

    return dp[n - 1][m - 1]

def main():
    with open("editdist.in", "r") as fin, open("editdist.out", "w") as fout:
        string1, string2 = fin.read().split()

        fout.write(str(levenshtein_dist(string1, string2)))


if __name__ == "__main__":
    main()