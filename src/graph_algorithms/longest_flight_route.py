from collections import deque
def task():
    n, m = map(int, input().split())
    graph = dict()
 
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a] = graph.get(a, list()) + [b]
 
    distances = [1 for _ in range(n + 1)]   
    parent = [i for i in range(n + 1)]
 
    def bfs(start):
        count = 0
        queue = deque()
        queue.append(start)
        while queue:
            current = queue.popleft()
            count += 1
            if count > n**2:
                return False
            for neighbour in graph.get(current, list()):
                if distances[neighbour] < distances[current] + 1:
                    distances[neighbour] = distances[current] + 1
                    queue.append(neighbour)
                    parent[neighbour] = current
        return True
    if not bfs(1):
        print("IMPOSSIBLE")
        return
    if distances[n] == 1:
        print("IMPOSSIBLE")
        return
    path = [n]
 
    current = n
    while current != 1:
        path.append(parent[current])
        current = parent[current]
 
 
    print(distances[n])
    print(" ".join(map(str, path[::-1])))
task()

