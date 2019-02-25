class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if N == 1 and not trust:
            return 1
        
        graph = [0 for i in range(N)]
        for a, b in trust:
            graph[a - 1] -= 1
            graph[b - 1] += 1
        
        for i, v in enumerate(graph):
            if v == N - 1:
                return i + 1
        return -1
