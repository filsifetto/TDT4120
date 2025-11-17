n, m = map(int, input().split())
 
from collections import deque
 
ds = []
 
for i in range(n):
    tmp = []
    word = input()
    for c in word:
        if c == "#":
            tmp.append(False)
        else:
            tmp.append(True)
    ds.append(tmp)
 
visited = [[False for _ in range(m)] for i in range(n)]
 
def bfs(i, j, ds):
    global visited
    queue = deque()
    # mark the starting cell visited and only start from open cells
    if not ds[i][j] or visited[i][j]:
        return
    visited[i][j] = True
    queue.append((i, j))
    visited[i][j] = True
 
    while queue:
        p, q = queue.popleft()
 
        if p != 0:
            if not visited[p - 1][q] and ds[p-1][q]:
                queue.append((p - 1, q))
                visited[p - 1][q] = True
        if q != 0:
            if not visited[p][q - 1] and ds[p][q - 1]:
                queue.append((p, q - 1))
                visited[p][q - 1] = True
        if p != n - 1:
            if not visited[p + 1][q] and ds[p + 1][q]:
                queue.append((p + 1, q))
                visited[p + 1][q] = True
        if q != m - 1:
            if not visited[p][q + 1] and ds[p][q + 1]:
                queue.append((p, q + 1))
                visited[p][q + 1] = True
 
 
count = 0
for i in range(n):
    for j in range(m):
        # only start BFS/count for unopened, open cells
        if not visited[i][j] and ds[i][j]:
            bfs(i, j, ds)
            count += 1
 
print(count)

