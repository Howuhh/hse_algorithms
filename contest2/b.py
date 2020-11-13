
def golden_knapsack(weights, S):
    dp = [[0] * (len(weights) + 1) for _ in range(S + 1)]

    for w in range(1, S + 1):
        for i in range(1, len(weights) + 1):
            dp[w][i] = dp[w][i - 1]
            w_i = weights[i - 1]

            if w_i <= w:
                dp[w][i] = max(dp[w][i - 1], dp[w - w_i][i - 1] + w_i)
    
    return dp[S][len(weights)]


def main():
    with open("knapsack.in", "r") as fin, open("knapsack.out", "w") as fout:
        S, N = map(int, fin.readline().split())
        gold = [int(i) for i in fin.readline().split()]

        fout.write(str(golden_knapsack(gold, S)))


if __name__ == "__main__":
    main()