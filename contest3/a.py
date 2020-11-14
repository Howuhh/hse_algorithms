import sys, threading

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def dfs(adj):
    visited = [0] * len(adj)
    p = [-1] * len(adj)
    
    cycle_path = []
    
    def _dfs(node):
        if cycle_path:
            return      
        visited[node] = 1

        for neigh in adj[node]:
            if visited[neigh] == 0:
                p[neigh] = node
                _dfs(neigh)
            elif visited[neigh] == 1:
                if not cycle_path:
                    head = node
                    cycle_path.append(head)
                    while head != neigh:
                        head = p[head]
                        cycle_path.append(head)
                    
        visited[node] = 2        

    for root in range(len(adj)):
        if visited[root] == 0:
            _dfs(root)

    return cycle_path[::-1]


def main():
    N, M = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(N)]
    
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
    
    cycle_path = dfs(adj)
    
    if cycle_path:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(str(i + 1) for i in cycle_path) + "\n")
    else:
        sys.stdout.write("NO\n")
    

if __name__ == "__main__":
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
    # main()
    
    
