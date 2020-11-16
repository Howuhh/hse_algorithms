import sys

from math import inf
from collections import deque

def bfs(exits, adj):
    p = list(range(len(adj)))
    dist = [inf] * len(adj)
     
    visited = [False] * len(adj)
    
    queue = deque(exits)
    for ex in exits:
        visited[ex] = True
        dist[ex] = 0
        
    while queue:
        node = queue.pop()
        
        for neigh in adj[node]:
            if not visited[neigh]:
                p[neigh] = p[node]
                visited[neigh] = True
                dist[neigh] = dist[node] + 1
                queue.appendleft(neigh)
            else:
                if dist[node] + 1 < dist[neigh] or (dist[node] + 1 == dist[neigh] and p[node] < p[neigh]):
                    dist[neigh] = dist[node] + 1
                    p[neigh] = p[node]
                    
    return dist, [i + 1 for i in p]


def main():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    
    exits = [int(i) - 1 for i in sys.stdin.readline().split()]

    M = int(sys.stdin.readline())
    adj = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    
    dist, p = bfs(exits, adj)
    print(*dist)
    print(*p)


if __name__ == "__main__":
    main()