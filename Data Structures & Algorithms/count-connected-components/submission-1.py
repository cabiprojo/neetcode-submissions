class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create an adjacency list
        adj = [[] for _ in range(n)]

        # fill in adj
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = set()

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)

            return 

        count = 0
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)

        return count

