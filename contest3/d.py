from math import inf

import heapq
import sys

def dijkstra_shortest(root, adj):
    dist = [inf] * len(adj)
    visited = [False] * len(adj)
    
    dist[root] = 0

    queue = [(0, root)]
    heapq.heapify(queue)
    
    while queue:
        _, node = heapq.heappop(queue)
        
        if visited[node]:
            continue
        visited[node] = True
        
        for t, w in adj[node]:
            if dist[node] + w < dist[t]:
                dist[t] = dist[node] + w
                heapq.heappush(queue, (dist[t], t))

    return dist
    

def main():
    N, S, F = map(int, sys.stdin.readline().split())
    
    adj = [[] for _ in range(N)]
    
    for i in range(N):
        line = sys.stdin.readline().split()
        
        for j in range(N):
            if j != i and int(line[j]) != -1:
                adj[i].append((j, int(line[j])))
              
    dist = dijkstra_shortest(S - 1, adj)
    print(-1 if dist[F - 1] == inf else dist[F - 1])
    

if __name__ == "__main__":
    main()