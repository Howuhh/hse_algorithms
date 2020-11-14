import sys

from collections import deque

def bfs(root, exits, adj):
    visited = [False] * len(adj)
    dist = [0] * len(adj) 
    
    queue = deque([root])
    visited[root] = True
    
    while queue:
        node = queue.pop()
        
        for neigh in adj[node]:
            if not visited[neigh]:
                visited[neigh] = True
                dist[neigh] = dist[node] + 1
                
                if neigh in exits:
                    return (dist[neigh], neigh + 1)
                
def min_dist_exit(exits, adj):
    dist = [0] * len(adj)
    ex = list(range(1, len(adj) + 1))

    for i in range(len(adj)):
        if i not in exits:
            min_dist = bfs(i, exits, adj)
            dist[i] = min_dist[0]
            ex[i] = min_dist[1]
        
    print(*dist)
    print(*ex)

def main():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    
    exits = set()
    for _ in range(K):
        exits.add(int(sys.stdin.readline()) - 1)
        
    M = int(sys.stdin.readline())
    adj = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    
    min_dist_exit(exits, adj)


if __name__ == "__main__":
    main()