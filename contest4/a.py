import sys
import heapq

def lazy_prim(adj, n):
    visited = [False] * n
    
    mst_weight = 0
    mst_nodes = 0
    
    queue = [(0, 0)]
    
    while queue and mst_nodes < n:
        w, node = heapq.heappop(queue)
        
        if visited[node]:
            continue
        
        visited[node] = True
        
        mst_nodes = mst_nodes + 1
        mst_weight = mst_weight + w
        
        for neigh, w_n in adj[node]:
            if not visited[neigh]:
                heapq.heappush(queue, (w_n, neigh))
                    
    return mst_weight

def main():
    n, m = map(int, sys.stdin.readline().split())
    
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        b, e, w = map(int, sys.stdin.readline().split())
        adj[b - 1].append((e - 1, w))
        adj[e - 1].append((b - 1, w))
        
    print(lazy_prim(adj, n))

if __name__ == "__main__":
    main()