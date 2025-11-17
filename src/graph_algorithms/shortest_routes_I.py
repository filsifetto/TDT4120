from math import inf
import heapq
from itertools import count
 
class UpdatablePriorityQueue:
    """
    Min-priority queue with O(log n) push/update/pop.
    Items must be hashable.
    """
    __slots__ = ("_heap", "_prio", "_seq")
 
    def __init__(self):
        self._heap = []                 # stores (priority, seq, item)
        self._prio = {}                 # item -> current priority
        self._seq  = count()            # tie-breaker to avoid comparing items
 
    def __len__(self):
        return len(self._prio)
 
    def push(self, item, priority):
        """Insert a new item or overwrite its priority (same as update)."""
        self._prio[item] = priority
        heapq.heappush(self._heap, (priority, next(self._seq), item))
 
    def update(self, item, priority):
        """Change an item's priority (decrease or increase)."""
        self.push(item, priority)
 
    def remove(self, item):
        """Logically delete an item if present. Returns True if it existed."""
        return self._prio.pop(item, None) is not None
 
    def peek(self):
        """Look at the current minimum without removing it."""
        self._discard_stale()
        if not self._heap:
            raise KeyError("peek from an empty queue")
        prio, _, item = self._heap[0]
        return item, prio
 
    def pop(self):
        """Remove and return the (item, priority) pair with minimum priority."""
        self._discard_stale()
        if not self._heap:
            raise KeyError("pop from an empty queue")
        prio, _, item = heapq.heappop(self._heap)
        # This entry is guaranteed fresh because of _discard_stale()
        self._prio.pop(item, None)
        return item, prio
 
    def _discard_stale(self):
        """Throw away heap top entries that don't match current priorities."""
        while self._heap:
            prio, _, item = self._heap[0]
            if self._prio.get(item) == prio:
                return                      # top is fresh
            heapq.heappop(self._heap)       # drop stale entry
 
 
def task():
    n, m = map(int, input().split())
 
    graph = dict()
 
    for i in range(m):
        a, b, dist = map(int, input().split())
 
        graph[a] = graph.get(a, list()) + [(b, dist)]
 
 
    def dijkstras(start):
        distance = [inf for _ in range(n + 1)]
        distance[start] = 0
        
        pq = UpdatablePriorityQueue()
 
        pq.push(start, 0)
 
 
        while pq:
            cur_node, cur_dist = pq.pop()
 
            for node, weight in graph.get(cur_node, list()):
                if cur_dist + weight < distance[node]:
                    distance[node] = cur_dist + weight
                    pq.push(node, distance[node])
        
        return distance[1:]
    
    distances = dijkstras(1)
    print(" ".join(list(map(str, distances))))
 
task()

