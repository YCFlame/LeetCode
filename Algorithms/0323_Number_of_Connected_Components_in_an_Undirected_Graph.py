class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for f, t in edges:
            graph[f].append(t)
            graph[t].append(f)
        
        visited = set()
        count = 0
        from collections import deque
        for v, es in graph.items():
            if v not in visited:
                count += 1
                queue = deque([v])
                while queue:
                    x = queue.popleft()
                    if x not in visited:
                        visited.add(x)
                        queue.extend(graph[x])
        
        return count
                
            
