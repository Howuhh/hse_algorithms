import sys
import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        
    def union(self, a, b):        
        a = self.find(a)
        b = self.find(b)
        
        if a != b:
            if self.rank[a] < self.rank[b]:
                a, b = b, a
                
            self.parent[b] = a
                                    
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1       
    
    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def same(self, a, b):
        return self.find(a) == self.find(b)
    
    
def kruskal_mst(edges, n):
    union = UnionFind(n)
    edges = sorted(edges, key=lambda t: t[2])
    
    mst_adj = [[] for _ in range(n)]
    
    for f, t, w in edges:
        if not union.same(f, t):
            union.union(f, t)
            
            mst_adj[f].append((t, w))
            mst_adj[t].append((f, w))
    
    return mst_adj


def dfs(adj, start, points, H):
    visited = [False] * len(adj)
    
    max_d = []
    def _dfs(root, max_w):
        nonlocal max_d
            
        if points[root][1] == H:
            max_d.append(max_w)

        for node, w in adj[root]:
            if not visited[node]:
                visited[node] = True 
                _dfs(node, max(max_w, w)) 
            
    visited[start] = True
    _dfs(start, -1)
    
    return min(max_d)
    

def main():
    H, N = map(int, sys.stdin.readline().split())
    points = []

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))
        points.append((x, 0))
        points.append((x, H))
        
    edges = []
    for p1 in range(len(points)):
        for p2 in range(len(points)):
            if p1 < p2:
                d = dist(points[p1], points[p2])
                    
                edges.append((p1, p2, d))
                edges.append((p2, p1, d))
        
    mst = kruskal_mst(edges, len(points))

    min_max = math.inf
    for i, point in enumerate(points):
        if point[1] == 0:
            min_max = min(min_max, dfs(mst, i, points, H))

    print(round(min_max, 9))
            

if __name__ == "__main__":
    main()