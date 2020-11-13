from collections import deque


def topological_sort(adj, indegree):
    topsort = []
    
    queue = deque([a for a in range(len(adj)) if indegree[a] == 0])
    
    while queue:
        node = queue.pop()
        
        for neigh in adj[node]:
            indegree[neigh] -= 1
            
            if indegree[neigh] == 0:
                queue.appendleft(neigh)
            
        topsort.append(node)
    
    return topsort


def longest_path(adj, indegree):
    topsort = topological_sort(adj, indegree)
    
    dist = [0] * len(adj)
    for v in topsort[::-1]:
        for u in adj[v]:
            dist[v] = max(dist[v], dist[u] + 1)

    return max(dist)


def main():
    with open("longpath.in", "r") as fin, open("longpath.out", "w") as fout:
        n, m = map(int, fin.readline().split())
        
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        
        for _ in range(m):
            a, b = map(int, fin.readline().split())
            
            adj[a - 1].append(b - 1)
            indegree[b - 1] += 1
            
        fout.write(str(longest_path(adj, indegree)))
        


if __name__ == "__main__":
    main()