from collections import deque
 
def task():
    n, m = map(int, input().split())
    grid = [[False] * (m + 2) for _ in range(n + 2)]
    start = None
    target = (-1, -1)
 
    for i in range(1, n + 1):
        line = input().strip()
        for j in range(1, m + 1):
            c = line[j-1]
            if c == '#':
                grid[i][j] = False
            else:
                grid[i][j] = True
                if c == 'A':
                    start = (i, j)
                elif c == 'B':
                    target = (i, j)
                    # we don't need to store B specially; we just check grid
                    pass
 
    # parent[y][x] = (py, px, move_char) that leads from parent -> (y,x)
    parent = [[None] * (m + 2) for _ in range(n + 2)]
    visited = [[False] * (m + 2) for _ in range(n + 2)]
 
    def bfs(sy, sx):
        dq = deque()
        dq.append((sy, sx))
        visited[sy][sx] = True
        parent[sy][sx] = (None, None, '')  # sentinel
 
        while dq:
            y, x = dq.popleft()
            # check if this is B
            # We need a way to detect B: we can either read input again, or have a separate grid marking B
            # Let's just check the original input or store a flag. For simplicity assume grid_B flag array.
            if (y, x) == target:  # you should set `target` when reading
                # found, now build path
                path = []
                cy, cx = y, x
                while parent[cy][cx][0] is not None:
                    py, px, move = parent[cy][cx]
                    path.append(move)
                    cy, cx = py, px
                path.reverse()
                return ''.join(path), len(path)
 
            for dy, dx, move in [(-1,0,'U'), (1,0,'D'), (0,-1,'L'), (0,1,'R')]:
                ny, nx = y + dy, x + dx
                if not visited[ny][nx] and grid[ny][nx]:
                    visited[ny][nx] = True
                    parent[ny][nx] = (y, x, move)
                    dq.append((ny, nx))
        return None, -1
 
    # You need to set `target = (ty, tx)` when reading input if c == 'B'
    # For example, during input loop:
    #    if c == 'B': target = (i,j)
 
    path, dist = bfs(start[0], start[1])
 
    if dist == -1:
        print("NO")
    else:
        print("YES")
        print(dist)
        print(path)
 
task()
