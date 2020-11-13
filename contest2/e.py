from math import inf
from pprint import pprint

def in_set(mask, index):
    return (mask >> index) & 1

def diff_set(mask, index):
    return mask & (~(1 << index))

def tsp(w):
    N = len(w)
    
    dp = [[inf] * 2**N for _ in range(N)]
    prev = [[(-1, -1)] * 2**N for _ in range(N)]
    
    dp[0][1] = 0
    
    for S in range(1, 1 << N):
        for v in range(N):

            if in_set(S, 0) and in_set(S, v):
                for u in range(N):
                    if in_set(S, u) and u != v:
                        S_not_v = diff_set(S, v)
                        
                        if dp[u][S_not_v] + w[u][v] < dp[v][S]:
                            dp[v][S] = dp[u][S_not_v] + w[u][v]
                            prev[v][S] = (u, S_not_v)
    
    min_dist = inf
    for u in range(1, N):
        if dp[u][(1 << N) - 1] < min_dist:
            min_dist = dp[u][(1 << N) - 1]
            last = (u, (1 << N) - 1)

    path = []
    while last != (-1, -1):
        path.append(last[0] + 1)
        last = prev[last[0]][last[1]]
    
    return min_dist, path


def main():
    with open("aquarium.in", "r") as fin, open("aquarium.out", "w") as fout:
        n = int(fin.readline())
        
        if n == 1:
            fout.write(str(0) + "\n")
            fout.write(str(0))
            return
        
        adj_mat = []
        
        for _ in range(n):
            adj_mat.append([int(j) for j in fin.readline().split()])
            
        min_dist, path = tsp(adj_mat)

        fout.write(str(min_dist) + "\n")
        fout.write(" ".join([str(i) for i in path]))


if __name__ == "__main__":
    main()