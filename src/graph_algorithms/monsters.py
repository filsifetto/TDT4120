from collections import deque
from math import inf
 
def task():
    n, m = map(int, input().split())
 
    grid = [[False for _ in range(m + 2)] for i in range(n + 2)]
    monsters = list()
    start = (-1, -1)
 
    for i in range(m + 2):
        grid[0][i] = "B"
        grid[-1][i] = "B"
    
    for i in range(n + 2):
        grid[i][0] = "B"
        grid[i][-1] = "B"
     
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
                elif c == 'M':
                    monsters.append((i, j))
                    pass
 
    monster_times = [[inf for _ in range(m + 2)] for j in range(n + 2)]
 
    def simultaneous_bfs(monsters):
        time = 0
        queues = [deque() for _ in range(len(monsters))]
        all_empty = False
        
 
        visited = [[False for _ in range(m + 2)] for i in range(n + 2)] 
 
        for i in range(len(monsters)):
            queues[i].append((monsters[i][0], monsters[i][1], 0))
        for i, j in monsters:
            visited[i][j] = True
            monster_times[i][j] = 0
        
        while not all_empty:
            all_empty = True
            for q in queues:
                if q:
                    all_empty = False
                    current_i, current_j, time = q.popleft()
                    if grid[current_i][current_j] == 'B':
                        q.clear()
                        continue
                    else:
                        for dy, dx in [(0,1), (0,-1), (1, 0), (-1, 0)]:
                            if visited[current_i + dy][current_j + dx] or not grid[current_i + dy][current_j + dx]:
                                continue
                            if grid[current_i + dy][current_j + dx] == 'B':
                                continue
                            visited[current_i + dy][current_j + dx] = True
                            monster_times[current_i + dy][current_j + dx] = time + 1
                            q.append((current_i + dy, current_j + dx, time + 1))
 
        
 
 
    def bfs_single(start):
        queue = deque()
        queue.append((start[0], start[1], 0, ""))
        visited = [[False for _ in range(m + 2)] for j in range(n + 2)]
        visited[start[0]][start[1]] = True
        
        while queue:
            current_i, current_j, time, path = queue.popleft()
            for dy, dx, direction in [(0,1, "R"), (0,-1, "L"), (1, 0, "D"), (-1, 0, "U")]:
                # print(direction)
                if not visited[current_i + dy][current_j + dx] and grid[current_i + dy][current_j + dx]:
                    if grid[current_i + dy][current_j + dx] == 'B':
                        return time, path
                    if monster_times[current_i + dy][current_j + dx] > time + 1:
                        visited[current_i + dy][current_j + dx] = True
                        queue.append((current_i + dy, current_j + dx, time + 1, path + direction))
        return -1, -1
    simultaneous_bfs(monsters)
    time, path = bfs_single(start)
    if time == -1:
        print("NO")
        return
    else:
        print("YES")
        print(time)
        print(path)
task()

