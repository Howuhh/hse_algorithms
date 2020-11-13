from collections import deque

def graph_components(adj):
    count = 0
    visited = [False] * len(adj)
    components = [-1] * len(adj)

    def bfs(root):
        queue = deque([root])

        visited[root] = True
        components[root] = count

        while queue:
            node = queue.pop()

            for neigh in adj[node]:
                if not visited[neigh]:
                    queue.appendleft(neigh)
                    visited[neigh] = True
                    components[neigh] = count

    for node in range(len(adj)):
        if not visited[node]:
            count = count + 1
            bfs(node)
    
    return count, components


def main():
    with open("connect.in", "r") as fin, open("connect.out", "w") as fout:
        N, M = map(int, fin.readline().split())

        adj = [[] for _ in range(N)]
        for i in range(M):
            a, b = [int(i) - 1 for i in fin.readline().split()]
            adj[a].append(b)
            adj[b].append(a)

        count, components = graph_components(adj)

        fout.write(str(count) + "\n")
        fout.write(" ".join([str(i) for i in components]))

if __name__ == "__main__":
    main()