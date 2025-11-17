from collections import deque
 
def task():
    n, x = map(int, input().split())
 
    A = list(map(int, input().split()))
    A.sort()
    queue = deque()
 
    visited = [False for _ in range(x + 1)]
    visited[0] = True
    queue.append((0,0))
 
    while queue:
        current, distance = queue.popleft()
        for v in A:
            if current + v == x:
                print(distance + 1)
                return
            if current + v > x:
                break
            if visited[current + v]:
                continue
            visited[current + v] = True
            queue.append((current + v, distance + 1))
    print(-1)
        
task()

