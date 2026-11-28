class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        # locates the root representative of a node's group
        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res
        
        # merges two separate groups into one
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


        ''' DFS approach
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

        count = 0
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)

        return count
        '''
