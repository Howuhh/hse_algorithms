import sys
from math import inf


def floyd_warshall(adj_matrix, N):
    dist = adj_matrix.copy()
    
    for k in range(N):
        for i in range(N):            
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    return dist

def main():
    N = int(sys.stdin.readline())
    
    adj_matrix = [[inf] * N for _ in range(N)]
    
    for i in range(N):
        line = sys.stdin.readline().split()
        for j in range(N):
            if int(line[j]) != -1:
                adj_matrix[i][j] = 0 if i == j else int(line[j])
                
    dist = floyd_warshall(adj_matrix, N)
    print(max(sum(dist, [])))
    
    rad = inf
    for i in range(N):
        rad = min(rad, max(dist[i]))
    print(rad)
    
    
    

if __name__ == "__main__":
    main()