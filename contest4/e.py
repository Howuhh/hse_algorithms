import sys
import math
import threading

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

class Edge:
    def __init__(self, a, b, f, c):
        self.a, self.b, self.f, self.c = a, b, f, c
        
class Graph:
    def __init__(self, n, s, t):
        self.n, self.s, self.t = n, s, t
        self.adj = [[] for _ in range(n)]
        self.edges = []
        
    def add_edge(self, a, b):
        self.adj[a].append(len(self.edges))
        self.edges.append(Edge(a, b, 0, 1))
        self.adj[b].append(len(self.edges))
        self.edges.append(Edge(b, a, 0, 0))
    
    def dfs(self, node):   
        self.visited[node] = self.counter     
        
        if node == self.t:
            return True
        
        for e_idx in self.adj[node]:
            edge, back_edge = self.edges[e_idx], self.edges[e_idx ^ 1]
            
            if edge.f < edge.c and self.visited[edge.b] != self.counter and self.dfs(edge.b):
                edge.f += 1
                back_edge.f -= 1
                return True
        
        return False

    def dfs_residual(self, node):
        head = node
        
        while head != self.t:
            print(head + 1, end=" ")
            for e_idx in self.adj[head]:
                edge = self.edges[e_idx]
                
                if edge.f == 1:
                    edge.f -= 1
                    head = edge.b
                    break
        print(self.t + 1)

    
    def ford_fulkerson(self):
        self.counter = 0
        self.visited = [-1] * self.n
        
        while self.dfs(self.s):
            self.counter += 1
            if self.counter == 2:
                break
            
        if self.counter == 2:
            print("YES")
            self.dfs_residual(self.s)
            self.dfs_residual(self.s)
        else:
            print("NO")


def main():
    n, m, s, t = [int(i) for i in sys.stdin.readline().split()]
    
    graph = Graph(n, s - 1, t - 1)
    for _ in range(m):
        a, b = [int(i) for i in sys.stdin.readline().split()]
        graph.add_edge(a - 1, b - 1)
        
    graph.ford_fulkerson()


if __name__ == "__main__":
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()