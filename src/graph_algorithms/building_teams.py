from collections import deque
 
def task():
    n, m = map(int, input().split())
 
    graph = dict()
 
    for i in range(m):
        a, b = map(int, input().split())
 
        graph[a] = graph.get(a, list()) + [b]
        graph[b] = graph.get(b, list()) + [a]
 
    colours = [None for _ in range(n + 1)]
 
    def bfs(start):
        queue = deque()
        queue.append((start, True))
        colours[start] = True
 
        while queue:
            current, colour = queue.popleft()
            for node in graph.get(current, list()):
                if colours[node] == None:
                    colours[node] = not colour
                    queue.append((node, not colour))
                elif colours[node] == colour:
                    print("IMPOSSIBLE")
                    return False
        return True
    for i in range(1, n + 1):
        if colours[i] == None:
            if not bfs(i):
                return
 
    for i in range(1, n + 1):
        if colours[i]:
            print(1, end = " ")
        else:
            print(2, end = " ")
 
task()

