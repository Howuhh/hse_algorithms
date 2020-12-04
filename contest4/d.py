import sys
import math

class Edge:
    def __init__(self, a, b, f, c, idx):
        self.a, self.b = a, b
        self.f, self.c = f, c
        self.idx = idx
        
        
class Graph:
    def __init__(self, n, s, t):
        self.n, self.s, self.t = n, s, t
        self.edge_idx = 1
        
        self.adj = [[] for _ in range(n)]
        self.edges = []

    def add_edge(self, a, b, c):
        
        self.adj[a].append(len(self.edges))
        self.edges.append(Edge(a, b, 0, c, self.edge_idx))        
        self.adj[b].append(len(self.edges))
        self.edges.append(Edge(b, a, 0, c, self.edge_idx))
        self.edge_idx = self.edge_idx + 1
                
        
    def dfs(self, root, min_cap):   
        self.visited[root] = self.counter     
        
        if root == self.t:
            return True, min_cap
        
        for e_idx in self.adj[root]:
            edge, back_edge = self.edges[e_idx], self.edges[e_idx ^ 1]

            if edge.f < edge.c and self.visited[edge.b] != self.counter:
                min_cap = min(min_cap, (edge.c - edge.f))
                
                path, min_on_path = self.dfs(edge.b, min_cap)
                
                if path:
                    edge.f += min_on_path
                    back_edge.f -= min_on_path
                
                    return True, min_on_path     
        
        return False, 0
        
    def ford_fulkerson(self):
        self.visited = [-1] * self.n
        self.counter = 0
        
        flow_size = 0
        
        while True:
            res_path, flow = self.dfs(self.s, math.inf)
            if not res_path:
                break
            
            flow_size = flow_size + flow
            self.counter = self.counter + 1
        
        # find min cut edges -> all that from visited to not visited (bcs capacity 0)   
        edge_cut = []
        for edge in self.edges:
            if self.visited[edge.a] == self.counter and self.visited[edge.b] != self.counter:
                edge_cut.append(edge.idx)

        return flow_size, edge_cut


def main():
    n, m = map(int, sys.stdin.readline().split())
    
    graph = Graph(n, 0, n - 1)
    
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph.add_edge(a - 1, b - 1, c)

    max_flow, min_cut = graph.ford_fulkerson()
    
    print(len(min_cut), max_flow)
    print(*min_cut)

if __name__ == "__main__":
    main()