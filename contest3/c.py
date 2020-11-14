import sys

from collections import deque

all_moves = [
    [-1, -2], [-2, -1], 
    [-1, 2], [2, -1], 
    [1, -2], [-2, 1], 
    [1, 2], [2, 1]
]
letters = ["a", "b", "c", "d", "e", "f", "g", "h"] 
let_map = {let:i for i, let in enumerate(letters)}
          
  
def bfs(start, end):
    path = 0
    
    visited = [[False] * 8 for _ in range(8)]
    p = [[(-1, -1)] * 8 for _ in range(8)]
    queue = deque([start])
    
    while queue:
        x, y = queue.pop()
        # print(x, y)
        for (i, j) in all_moves:
            xx, yy = x + i, y + j
            
            if (xx < 0 or xx > 7) or (yy < 0 or yy > 7):
                continue
            
            if not visited[xx][yy]:
                visited[xx][yy] = True
                p[xx][yy] = (x, y)
                queue.appendleft([xx, yy])
                
            if (xx, yy) == end:
                path = [f"{letters[xx]}{yy + 1}"]
                while (xx, yy) != start:
                    xx, yy = p[xx][yy]
                    path.append(f"{letters[xx]}{yy + 1}")
                
                return path[::-1]

    return []
    

def main():
    start = list(sys.stdin.readline())
    end = list(sys.stdin.readline())

    x, y = let_map[start[0]], int(start[1]) - 1
    a, b = let_map[end[0]], int(end[1]) - 1
     
    shortest_path = bfs((x, y), (a, b))

    if shortest_path:
        [print(i) for i in shortest_path]
    

if __name__ == "__main__":
    main()