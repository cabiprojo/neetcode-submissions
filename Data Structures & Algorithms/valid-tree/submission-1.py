class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(n, parent):
            if n in visited:
                return False
            
            visited.add(n)
            for neighbor in adj[n]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, n): 
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
