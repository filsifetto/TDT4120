def task():
    n, m = map(int, input().split())
 
    graph = dict()
 
    for i in range(m):
        a, b = map(int, input().split())
 
        graph[a] = graph.get(a, list()) + [b]
        graph[b] = graph.get(b, list()) + [a]
 
    visited = [False for _ in range(n + 1)]
    parents = [-1 for _ in range(n + 1)]
 
    def dfs(start, parent):
 
        visited[start] = True
        parents[start] = parent
 
        stack = list()
        stack.append((start, parent))
 
        while stack:
            start, parent = stack.pop()
            visited[start] = True
            parents[start] = parent
        
            for node in graph.get(start, list()):
                if node == parent: #Siden vi har en urettet graf
                    continue
                elif not visited[node]:
                    stack.append((node, start))
                    # cycle = dfs(node, start)
                    # if cycle:
                    #     return cycle
                else:
                    current = start
                    path = [node, current]
                    while current != node:
                        current = parents[current]
                        path.append(current)
                    return path
        return False
        
    for i in range(1, n):
        if not visited[i]:
            cycle = dfs(i, -1)
            if cycle != False:
                print(len(cycle))
                for e in cycle:
                    print(e, end = " ")
                return
    print("IMPOSSIBLE")
    return
 
task()

