import sys

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.points = [0] * n
        
    def add(self, a, point):
        self.points[self.find(a)] += point
        
    def get(self, a):
        points_a = self.points[a]
        
        while a != self.parent[a]:
            a = self.parent[a]
            points_a += self.points[a]
            
        return points_a
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        
        if a != b:
            if self.rank[a] < self.rank[b]:
                a, b = b, a
                
            self.parent[b] = a
            self.points[b] -= self.points[a]
                        
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1            

    def find(self, a):
        if a != self.parent[a]:
            return self.find(self.parent[a])
        return a


def main():
    n, m = map(int, sys.stdin.readline().split())
    union = UnionFind(n)
    
    for _ in range(m):
        q = sys.stdin.readline().split()
        
        if q[0] == "add":
            a, v = int(q[1]) - 1, int(q[2])
            union.add(a, v)
        elif q[0] == "join":
            a, b = int(q[1]) - 1, int(q[2]) - 1
            union.union(a, b)
        elif q[0] == "get":
            a = int(q[1]) - 1
            print(union.get(a))
        

if __name__ == "__main__":
    main()